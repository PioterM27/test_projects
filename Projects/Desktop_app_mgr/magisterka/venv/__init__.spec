# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\KursAI\\pythonprojects\\venv\\magisterka_version2\\venv\\program\\main\\__init__.py'],
             pathex=['D:\\KursAI\\pythonprojects\\venv\\magisterka_version2\\venv\\Lib\\site-packages', 'D:\\KursAI\\pythonprojects\\venv\\magisterka_version2\\venv'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='__init__',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
