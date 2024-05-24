bl_info = {
    "name": "Copy Material Assignments",
    "blender": (2, 8, 0),
    "category": "Object",
}

import bpy
import bmesh

def copy_material_assignments(source, target):
    # Ensure both objects are in object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Get the material indices from the source object
    source_mesh = source.data
    source_material_indices = [polygon.material_index for polygon in source_mesh.polygons]

    # Assign materials to the target object
    target_mesh = target.data
    target_mesh.materials.clear()
    for material in source_mesh.materials:
        target_mesh.materials.append(material)

    # Ensure the target mesh has polygons
    if not target_mesh.polygons:
        bm = bmesh.new()
        bm.from_mesh(target_mesh)
        bm.to_mesh(target_mesh)
        bm.free()

    # Assign the material indices to the target object
    for i, polygon in enumerate(target_mesh.polygons):
        polygon.material_index = source_material_indices[i]

class OBJECT_OT_copy_material_assignments(bpy.types.Operator):
    bl_idname = "object.copy_material_assignments"
    bl_label = "Copy Material Assignments"
    bl_description = "Copy material assignments from the active object to the selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        source = context.active_object
        targets = [obj for obj in context.selected_objects if obj != source]

        for target in targets:
            copy_material_assignments(source, target)

        return {'FINISHED'}

def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(OBJECT_OT_copy_material_assignments.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_copy_material_assignments)
    bpy.types.VIEW3D_MT_make_links.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_copy_material_assignments)
    bpy.types.VIEW3D_MT_make_links.remove(menu_func)

if __name__ == "__main__":
    register()
