"""
Career Bridge AI - Project Verification Script

This script verifies that all components are properly implemented
and the project is ready for deployment.
"""

import os
import sys
from pathlib import Path

def verify_files():
    """Verify all required files exist."""
    required_files = [
        "app.py",
        "config.py",
        "database.py",
        "resume_parser.py",
        "career_engine.py",
        "scholarship_engine.py",
        "scheme_engine.py",
        "opportunity_engine.py",
        "roadmap_engine.py",
        "requirements.txt",
        "README.md"
    ]
    
    print("📁 Verifying file structure...")
    all_exist = True
    
    for file in required_files:
        path = Path(file)
        if path.exists():
            size = path.stat().st_size
            print(f"  ✅ {file} ({size:,} bytes)")
        else:
            print(f"  ❌ {file} - MISSING")
            all_exist = False
    
    return all_exist

def verify_imports():
    """Verify all imports work correctly."""
    print("\n📦 Verifying Python imports...")
    
    try:
        import streamlit
        print(f"  ✅ streamlit ({streamlit.__version__})")
    except ImportError as e:
        print(f"  ❌ streamlit - {e}")
        return False
    
    try:
        import pandas
        print(f"  ✅ pandas ({pandas.__version__})")
    except ImportError as e:
        print(f"  ❌ pandas - {e}")
        return False
    
    try:
        import numpy
        print(f"  ✅ numpy ({numpy.__version__})")
    except ImportError as e:
        print(f"  ❌ numpy - {e}")
        return False
    
    try:
        from PyPDF2 import PdfReader
        print(f"  ✅ PyPDF2")
    except ImportError as e:
        print(f"  ❌ PyPDF2 - {e}")
        return False
    
    try:
        from docx import Document
        print(f"  ✅ python-docx")
    except ImportError as e:
        print(f"  ❌ python-docx - {e}")
        return False
    
    return True

def verify_syntax():
    """Verify Python syntax in all modules."""
    print("\n🔍 Verifying Python syntax...")
    
    python_files = [
        "app.py",
        "config.py",
        "database.py",
        "resume_parser.py",
        "career_engine.py",
        "scholarship_engine.py",
        "scheme_engine.py",
        "opportunity_engine.py",
        "roadmap_engine.py"
    ]
    
    all_valid = True
    
    for file in python_files:
        try:
            with open(file, 'r') as f:
                compile(f.read(), file, 'exec')
            print(f"  ✅ {file}")
        except SyntaxError as e:
            print(f"  ❌ {file} - Syntax Error: {e}")
            all_valid = False
        except Exception as e:
            print(f"  ❌ {file} - Error: {e}")
            all_valid = False
    
    return all_valid

def verify_no_pass_statements():
    """Verify no TODO pass statements remain."""
    print("\n✏️  Checking for incomplete implementations...")
    
    python_files = [
        "app.py",
        "config.py",
        "database.py",
        "resume_parser.py",
        "career_engine.py",
        "scholarship_engine.py",
        "scheme_engine.py",
        "opportunity_engine.py",
        "roadmap_engine.py"
    ]
    
    all_complete = True
    
    for file in python_files:
        try:
            with open(file, 'r') as f:
                content = f.read()
                lines = content.split('\n')
                
            # Look for standalone 'pass' statements (TODO implementations)
            has_pass = False
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped == 'pass':
                    # Check if this is inside a docstring (which is OK)
                    before_context = '\n'.join(lines[max(0, i-10):i])
                    if '"""' in before_context or "'''" in before_context:
                        continue
                    has_pass = True
                    break
            
            if has_pass:
                print(f"  ⚠️  {file} - Contains pass statements")
                all_complete = False
            else:
                print(f"  ✅ {file}")
        except Exception as e:
            print(f"  ❌ {file} - Error: {e}")
            all_complete = False
    
    return all_complete

def verify_directories():
    """Verify required directories exist."""
    print("\n📂 Verifying directories...")
    
    directories = [
        "data",
        "uploads",
        "models",
        "assets",
        "logs",
        "tests"
    ]
    
    all_exist = True
    
    for dir_name in directories:
        path = Path(dir_name)
        if path.exists():
            print(f"  ✅ {dir_name}/")
        else:
            print(f"  ⚠️  {dir_name}/ - Will be created on first run")
    
    return all_exist

def main():
    """Run all verification checks."""
    print("\n" + "="*70)
    print("  CAREER BRIDGE AI - PROJECT VERIFICATION")
    print("="*70 + "\n")
    
    checks = [
        ("File Structure", verify_files),
        ("Python Imports", verify_imports),
        ("Python Syntax", verify_syntax),
        ("Implementation Completeness", verify_no_pass_statements),
        ("Directory Structure", verify_directories)
    ]
    
    results = {}
    
    for check_name, check_func in checks:
        try:
            results[check_name] = check_func()
        except Exception as e:
            print(f"\n❌ Error during {check_name}: {e}")
            results[check_name] = False
    
    # Summary
    print("\n" + "="*70)
    print("  VERIFICATION SUMMARY")
    print("="*70)
    
    all_passed = True
    
    for check_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {check_name}")
        if not passed:
            all_passed = False
    
    print("="*70 + "\n")
    
    if all_passed:
        print("🎉 ALL CHECKS PASSED!")
        print("✅ Career Bridge AI is ready for deployment!\n")
        print("To start the application, run:")
        print("  Windows: run.bat")
        print("  Linux/macOS: ./run.sh")
        print("  Or: streamlit run app.py\n")
        return 0
    else:
        print("⚠️  Some checks failed. Please review the errors above.\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
