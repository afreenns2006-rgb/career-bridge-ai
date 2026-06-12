"""
AI Provider module for Career Bridge AI.

Handles integration with AI services including Ollama (local)
and BYOK (Bring Your Own Key) support for external APIs.
"""

import requests
from typing import Optional, Dict, Any
import logging
from enum import Enum

logger = logging.getLogger(__name__)


class AIProvider(str, Enum):
    """Supported AI providers."""
    OLLAMA = "ollama"
    BYOK = "byok"


class OllamaProvider:
    """
    Local Ollama AI provider.
    
    Connects to Ollama running at http://localhost:11434
    """
    
    OLLAMA_API_URL = "http://localhost:11434/api/generate"
    DEFAULT_MODEL = "llama3"
    
    def __init__(self, model: str = DEFAULT_MODEL):
        """
        Initialize Ollama provider.
        
        Args:
            model: Ollama model name (default: llama3)
        """
        self.model = model
        self.api_url = self.OLLAMA_API_URL
    
    def check_connection(self) -> bool:
        """
        Check if Ollama is running and accessible.
        
        Returns:
            True if Ollama is running, False otherwise
        """
        try:
            response = requests.get(
                "http://localhost:11434/api/tags",
                timeout=5
            )
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            logger.error(f"Ollama connection error: {e}")
            return False
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 500
    ) -> Optional[str]:
        """
        Generate response using Ollama.
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text or None if error
        """
        if not self.check_connection():
            logger.error("Ollama is not running")
            return None
        
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
            
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "").strip()
            else:
                logger.error(f"Ollama error: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Ollama request error: {e}")
            return None
        except Exception as e:
            logger.error(f"Ollama error: {e}")
            return None
    
    def list_available_models(self) -> list[str]:
        """
        List available Ollama models.
        
        Returns:
            List of available model names
        """
        try:
            response = requests.get(
                "http://localhost:11434/api/tags",
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                models = data.get("models", [])
                return [m.get("name") for m in models if m.get("name")]
            return []
        except Exception as e:
            logger.error(f"Error listing Ollama models: {e}")
            return []


class BYOKProvider:
    """
    Bring Your Own Key (BYOK) provider.
    
    Allows users to provide their own API keys for external AI services.
    """
    
    def __init__(self, api_key: str, provider_type: str = "generic"):
        """
        Initialize BYOK provider.
        
        Args:
            api_key: API key for external service
            provider_type: Type of provider (generic, openai, anthropic, etc.)
        """
        self.api_key = api_key
        self.provider_type = provider_type
    
    def validate_key(self) -> bool:
        """
        Validate API key format.
        
        Returns:
            True if key format is valid
        """
        if not self.api_key or len(self.api_key) < 10:
            logger.error("Invalid API key format")
            return False
        return True
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 500
    ) -> Optional[str]:
        """
        Generate response using BYOK provider.
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text or None if error
            
        TODO: Implement BYOK provider integration
        - Support OpenAI API
        - Support Anthropic API
        - Support other popular LLM providers
        """
        if not self.validate_key():
            logger.error("Invalid API key")
            return None
        
        # Placeholder for BYOK implementation
        # In production, integrate with actual providers
        logger.info(f"BYOK provider not yet implemented for {self.provider_type}")
        return None


class AIService:
    """
    Main AI service coordinator.
    
    Manages different AI providers and routes requests appropriately.
    """
    
    def __init__(
        self,
        provider: AIProvider = AIProvider.OLLAMA,
        ollama_model: str = OllamaProvider.DEFAULT_MODEL,
        byok_api_key: Optional[str] = None
    ):
        """
        Initialize AI service.
        
        Args:
            provider: AI provider to use
            ollama_model: Model name for Ollama
            byok_api_key: API key for BYOK provider
        """
        self.provider = provider
        
        if provider == AIProvider.OLLAMA:
            self.service = OllamaProvider(ollama_model)
        elif provider == AIProvider.BYOK:
            if not byok_api_key:
                raise ValueError("BYOK provider requires API key")
            self.service = BYOKProvider(byok_api_key)
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def generate_career_advice(self, question: str) -> Optional[str]:
        """
        Generate career advice response.
        
        Args:
            question: Career question from user
            
        Returns:
            Career advice or None if error
        """
        prompt = f"""You are an expert career advisor. Answer the following career-related question concisely and helpfully.

Question: {question}

Provide practical advice and actionable recommendations."""
        
        return self.service.generate(prompt)
    
    def generate_resume_tips(self, resume_text: str) -> Optional[str]:
        """
        Generate resume improvement tips.
        
        Args:
            resume_text: Resume content
            
        Returns:
            Resume improvement tips or None if error
        """
        prompt = f"""As a professional resume writer, analyze this resume and provide 5-7 actionable improvement tips.

Resume:
{resume_text[:500]}...

Focus on: formatting, keywords, achievements, and ATS optimization."""
        
        return self.service.generate(prompt, max_tokens=400)
    
    def generate_interview_questions(self, job_title: str, skills: list[str]) -> Optional[str]:
        """
        Generate interview questions for a position.
        
        Args:
            job_title: Target job title
            skills: Relevant skills
            
        Returns:
            Interview questions or None if error
        """
        skills_str = ", ".join(skills[:5])
        prompt = f"""Generate 5-7 common interview questions for a {job_title} position with these skills: {skills_str}.

Include both technical and behavioral questions with brief tips for answering."""
        
        return self.service.generate(prompt, max_tokens=500)
    
    def generate_skill_recommendations(self, current_skills: list[str], target_career: str) -> Optional[str]:
        """
        Generate skill recommendations.
        
        Args:
            current_skills: Current skills
            target_career: Target career
            
        Returns:
            Skill recommendations or None if error
        """
        skills_str = ", ".join(current_skills[:5])
        prompt = f"""For someone with these skills ({skills_str}) wanting to become a {target_career}, recommend:
1. Top 5 skills to develop
2. Learning resources
3. Timeline for skill acquisition

Be specific and actionable."""
        
        return self.service.generate(prompt, max_tokens=400)
    
    def generate_project_suggestions(self, skills: list[str], level: str = "intermediate") -> Optional[str]:
        """
        Generate project suggestions.
        
        Args:
            skills: Available skills
            level: Experience level
            
        Returns:
            Project suggestions or None if error
        """
        skills_str = ", ".join(skills[:5])
        prompt = f"""Suggest 3-5 portfolio projects for a {level} developer with these skills: {skills_str}.

For each project, include:
- Project idea
- Learning outcomes
- Estimated duration
- Resource links"""
        
        return self.service.generate(prompt, max_tokens=500)
    
    def generate_learning_roadmap(self, target_career: str, current_level: str, duration_months: int) -> Optional[str]:
        """
        Generate personalized learning roadmap.
        
        Args:
            target_career: Target career path
            current_level: Current skill level
            duration_months: Desired duration
            
        Returns:
            Learning roadmap or None if error
        """
        prompt = f"""Create a {duration_months}-month learning roadmap for someone at {current_level} level aiming for a {target_career} role.

Include:
- Monthly goals
- Skills to learn
- Recommended resources
- Milestones
- Time commitment

Be realistic and comprehensive."""
        
        return self.service.generate(prompt, max_tokens=800)


def create_ai_service(
    provider: str,
    ollama_model: str = OllamaProvider.DEFAULT_MODEL,
    byok_api_key: Optional[str] = None
) -> Optional[AIService]:
    """
    Factory function to create AI service.
    
    Args:
        provider: Provider type ("ollama" or "byok")
        ollama_model: Ollama model name
        byok_api_key: BYOK API key
        
    Returns:
        AIService instance or None if error
    """
    try:
        if provider.lower() == "ollama":
            return AIService(AIProvider.OLLAMA, ollama_model)
        elif provider.lower() == "byok":
            if not byok_api_key:
                logger.error("BYOK provider requires API key")
                return None
            return AIService(AIProvider.BYOK, byok_api_key=byok_api_key)
        else:
            logger.error(f"Unknown provider: {provider}")
            return None
    except Exception as e:
        logger.error(f"Error creating AI service: {e}")
        return None
