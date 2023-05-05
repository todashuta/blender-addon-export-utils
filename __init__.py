bl_info = {
    "name": "Export Utils",
    "author": "Toda Shuta",
    "version": (0, 1, "0-dev"),
    "blender": (2, 93, 0),
    "location": "View 3D > Side Bar > Misc > Export Utility",
    "description": "Utility for Export Models (Substance Painter, etc.)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}


if "bpy" in locals():
    import importlib
    importlib.reload(export_util)
else:
    from . import export_util

import bpy


def register():
    export_util.register()


def unregister():
    export_util.unregister()


if __name__ == "__main__":
    register()
