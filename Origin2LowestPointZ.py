import bpy
import bmesh

# Get the active object
obj = bpy.context.active_object

# Ensure the object is in edit mode
bpy.ops.object.mode_set(mode='EDIT')

# Create a BMesh from the object
bm = bmesh.from_edit_mesh(obj.data)

# Find the lowest vertex on the Z axis
lowest_vertex = min(bm.verts, key=lambda v: v.co.z)

# Get the current origin location
origin_location = obj.location

# Set the new origin location with the Z coordinate of the lowest vertex
new_origin_location = (origin_location.x, origin_location.y, (obj.matrix_world @ lowest_vertex.co).z)

# Set the cursor to the new origin location
bpy.context.scene.cursor.location = new_origin_location

# Set the origin to the cursor location
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

# Update the mesh
#bmesh.update_edit_mesh(obj.data)
