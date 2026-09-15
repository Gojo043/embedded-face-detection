@echo off
:: run.bat - Face Recognition project launcher using Python 3.10
:: Usage:
::   run camera      - Test camera feed
::   run detect      - Test face detection
::   run landmark    - Test 5pt landmarks
::   run enroll      - Enroll a new person
::   run recognize   - Run live face recognition
::   run config      - Find camera index
::   run setup       - Create project folders (run once)
::   run install     - Install all dependencies

set PYTHON=C:\Users\Gloria\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python3.10.exe

if "%1"=="camera"    goto camera
if "%1"=="detect"    goto detect
if "%1"=="landmark"  goto landmark
if "%1"=="enroll"    goto enroll
if "%1"=="recognize" goto recognize
if "%1"=="config"    goto config
if "%1"=="setup"     goto setup
if "%1"=="install"   goto install

echo.
echo  Face Recognition Launcher
echo  -------------------------
echo  Usage: run [command]
echo.
echo  Commands:
echo    run setup       - Create project folders (run once)
echo    run install     - Install all dependencies
echo    run config      - Scan for camera indices
echo    run camera      - Test camera feed
echo    run detect      - Test Haar face detection
echo    run landmark    - Test 5pt landmark detection
echo    run enroll      - Enroll a new person into the DB
echo    run recognize   - Live face recognition
echo.
goto end

:setup
echo [setup] Creating project folders...
%PYTHON% init_project.py
goto end

:install
echo [install] Installing dependencies...
set SSL_CERT_FILE=
%PYTHON% -m pip install opencv-python numpy onnxruntime "mediapipe==0.10.21"
goto end

:config
echo [config] Scanning for cameras...
%PYTHON% -m src.config
goto end

:camera
echo [camera] Opening camera (index from config.py)...
%PYTHON% -m src.camera
goto end

:detect
echo [detect] Running face detection...
%PYTHON% -m src.detect
goto end

:landmark
echo [landmark] Running landmark detection...
%PYTHON% -m src.landmark
goto end

:enroll
echo [enroll] Starting enrollment...
%PYTHON% -m src.enroll
goto end

:recognize
echo [recognize] Starting face recognition...
%PYTHON% -m src.recognize
goto end

:end
