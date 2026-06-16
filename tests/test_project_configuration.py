from pathlib import Path

import config


def test_project_paths_are_inside_repository() -> None:
    root = config.PROJECT_ROOT.resolve()

    assert config.DATA_DIR.resolve().is_relative_to(root)
    assert config.UPLOADS_DIR.resolve().is_relative_to(root)
    assert config.MODELS_DIR.resolve().is_relative_to(root)
    assert config.LOGS_DIR.resolve().is_relative_to(root)


def test_get_config_exposes_upload_and_score_limits() -> None:
    settings = config.get_config()

    assert settings["max_upload_size_mb"] > 0
    assert ".pdf" in settings["allowed_formats"]
    assert settings["min_ats_score"] < settings["max_ats_score"]


def test_required_application_files_exist() -> None:
    expected_files = [
        "app.py",
        "career_engine.py",
        "resume_parser.py",
        "requirements.txt",
        "services/ai_provider.py",
        "services/language.py",
    ]

    for relative_path in expected_files:
        assert (Path(config.PROJECT_ROOT) / relative_path).exists()
