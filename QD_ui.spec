# QD_ui.spec — Generates ONLY ONE .exe file

# -*- mode: python -*-

block_cipher = None

a = Analysis(
    ['QD_ui.py'],          # main script
    pathex=['.'],          # search path for local modules
    binaries=[],
    datas=[('QD.tsp', '.')],  # include Keithley script into the .exe
    hiddenimports=[
        'TDK_PSU_Control',
        'matplotlib.backends.backend_tkagg',
        'tkinter.ttk',
        'tkinter.messagebox',
        'pyvisa',
        'numpy',
        'threading',
        'typing'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    a.zipfiles,

    # ONEFILE & WINDOWED ARE APPLIED HERE:
    name='QD_ui',
    icon=None,               # replace with 'QD.ico' if needed
    onefile=True,            # <<<<<<  IMPORTANT!
    console=False,           # console=False = windowed mode
    debug=False,
    upx=True,                # compress if UPX is installed
    strip=False,
)
