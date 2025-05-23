import os
import subprocess
import sys
import shutil


def run_pyinstaller_build():
    pyinstaller_command = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--icon=icons/app_icon.ico",
        "--name=Writing Tools",
        "--clean",
        "--noconfirm",
        # Exclude unnecessary modules
        "--exclude-module", "tkinter",
        "--exclude-module", "unittest",
        "--exclude-module", "IPython",
        "--exclude-module", "jedi",
        "--exclude-module", "email_validator",
        "--exclude-module", "cryptography",
        "--exclude-module", "psutil",
        "--exclude-module", "pyzmq",
        "--exclude-module", "tornado",
        # Exclude modules related to PySide6 that are not used
        "--exclude-module", "PySide6.QtNetwork",
        "--exclude-module", "PySide6.QtXml",
        "--exclude-module", "PySide6.QtQml",
        "--exclude-module", "PySide6.QtQuick",
        "--exclude-module", "PySide6.QtQuickWidgets",
        "--exclude-module", "PySide6.QtPrintSupport",
        "--exclude-module", "PySide6.QtSql",
        "--exclude-module", "PySide6.QtTest",
        "--exclude-module", "PySide6.QtSvg",
        "--exclude-module", "PySide6.QtSvgWidgets",
        "--exclude-module", "PySide6.QtHelp",
        "--exclude-module", "PySide6.QtMultimedia",
        "--exclude-module", "PySide6.QtMultimediaWidgets",
        "--exclude-module", "PySide6.QtOpenGL",
        "--exclude-module", "PySide6.QtOpenGLWidgets",
        "--exclude-module", "PySide6.QtPositioning",
        "--exclude-module", "PySide6.QtLocation",
        "--exclude-module", "PySide6.QtSerialPort",
        "--exclude-module", "PySide6.QtWebChannel",
        "--exclude-module", "PySide6.QtWebSockets",
        "--exclude-module", "PySide6.QtWinExtras",
        "--exclude-module", "PySide6.QtNetworkAuth",
        "--exclude-module", "PySide6.QtRemoteObjects",
        "--exclude-module", "PySide6.QtTextToSpeech",
        "--exclude-module", "PySide6.QtWebEngineCore",
        "--exclude-module", "PySide6.QtWebEngineWidgets",
        "--exclude-module", "PySide6.QtWebEngine",
        "--exclude-module", "PySide6.QtBluetooth",
        "--exclude-module", "PySide6.QtNfc",
        "--exclude-module", "PySide6.QtWebView",
        "--exclude-module", "PySide6.QtCharts",
        "--exclude-module", "PySide6.QtDataVisualization",
        "--exclude-module", "PySide6.QtPdf",
        "--exclude-module", "PySide6.QtPdfWidgets",
        "--exclude-module", "PySide6.QtQuick3D",
        "--exclude-module", "PySide6.QtQuickControls2",
        "--exclude-module", "PySide6.QtQuickParticles",
        "--exclude-module", "PySide6.QtQuickTest",
        "--exclude-module", "PySide6.QtQuickWidgets",
        "--exclude-module", "PySide6.QtSensors",
        "--exclude-module", "PySide6.QtStateMachine",
        "--exclude-module", "PySide6.Qt3DCore",
        "--exclude-module", "PySide6.Qt3DRender",
        "--exclude-module", "PySide6.Qt3DInput",
        "--exclude-module", "PySide6.Qt3DLogic",
        "--exclude-module", "PySide6.Qt3DAnimation",
        "--exclude-module", "PySide6.Qt3DExtras",
        "main.py"
    ]

    try:
        # Remove previous build directories
        for folder in ['dist', 'build', '__pycache__']:
            if os.path.exists(folder):
                shutil.rmtree(folder)

        # Run PyInstaller
        subprocess.run(pyinstaller_command, check=True)
        print("Build completed successfully!")

        # Copy resources to dist directory
        if not os.path.exists('dist'):
            os.makedirs('dist')

        # Copy "icons" folder
        shutil.copytree('icons', os.path.join('dist', 'icons'))
        
        # Copy files
        image_files = [
            "options.json",
            "background.png",
            "background_dark.png",
            "background_popup.png",
            "background_popup_dark.png"
        ]
        for file in image_files:
            if os.path.exists(file):
                shutil.copy(file, 'dist')
            else:
                print(f"Warning: {file} not found.")


        # Clean up unnecessary files
        for folder in ['build', '__pycache__']:
            if os.path.exists(folder):
                shutil.rmtree(folder)

    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_pyinstaller_build()