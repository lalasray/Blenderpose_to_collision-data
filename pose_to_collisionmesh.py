import bpy
from pathlib import Path

context = bpy.context
scene = context.scene
viewlayer = context.view_layer

start_frame = 0
end_frame = 8550
obs = [o for o in scene.objects if o.type == 'MESH']
bpy.ops.object.select_all(action='DESELECT')
    
for f in range(start_frame, end_frame,500): 
    scene.frame_set(f)
    path = Path("c:/Users/Lala/Desktop/stl")
    for ob in obs:
        if ob.name == "Plane":
            viewlayer.objects.active = ob
            ob.select_set(True)
            stl_path = path / f"{str(f)+ob.name}.stl"
            bpy.ops.export_mesh.stl(filepath=str(stl_path),use_selection=True)
            ob.select_set(False)