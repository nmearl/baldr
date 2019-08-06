# -*- mode: python -*-
import astropy
astropy_path, = astropy.__path__

block_cipher = None


a = Analysis(['py_shim.py'],
             pathex=['/Users/nearl/projects/baldr/utils'],
             binaries=[],
             datas=[(astropy_path, 'astropy')],
             hiddenimports=['ipykernel',
                            'ipykernel.datapub',
                            'IPython.extensions.storemagic',
                            'ipywidgets',
                            'jupyterlab_pygments',
                            'ipyvuetify',
                            'bqplot',
                            'numpy',
                            'scipy'],
             hookspath=['/Users/nearl/projects/baldr/hooks'],
             runtime_hooks=[],
             excludes=['tkinter', 'astropy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='py_shim',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='py_shim')
