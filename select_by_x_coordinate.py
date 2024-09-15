import bpy
import bmesh

bl_info = {
    "name": "Vertices selection by x-coordinate",
    "author": "Takuya Kazama",
    "version": (1,0),
    "blender": (3, 4, 1),
    "location": "View3D->select(Mesh EditMode)->Select by x-coordinate",
    "description": "select vertices by x-coordinate",
    "warning":"",
    "doc_url":"",
    "category": "Mesh",
}

class Operator_select_x_equal_to_or_bigger_than_zero(bpy.types.Operator):
    bl_idname = "object.select_x_equal_to_or_bigger_than_zero"
    bl_label = "select x >= 0"
    bl_description = "select vertices of x >= 0"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):  
                            # Get the active object
                        active_obj = bpy.context.active_object
                        
                        if active_obj is None or active_obj.type != 'MESH':
                            self.report({'INFO'}, "active object is not Mesh, process aborted")
                            return {'FINISHED'}
                        
                        if bpy.context.mode != 'EDIT':
                                bpy.ops.object.mode_set(mode='EDIT')
                                
                        bm = bmesh.from_edit_mesh(active_obj.data)
                        
                        if(bm is None):
                            self.report({'INFO'}, "bmesh is invalid, process aborted")
                            return {'FINISHED'}
                        
                        for vert in bm.verts:
                            vert.select = False 
                            
                        for edge in bm.edges:
                            edge.select = False
                        
                        for face in bm.faces:
                            face.select = False
                        
                        for vert in bm.verts:
                            if vert.co[0] > -0.0001:
                                    vert.select = True
                        bmesh.update_edit_mesh(active_obj.data)  
                        return {'FINISHED'}            
                                
class Operator_select_x_bigger_than_zero(bpy.types.Operator):
    bl_idname = "object.select_x_bigger_than_zero"
    bl_label = "select x > 0"
    bl_description = "select vertices of x > 0"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):  
                            # Get the active object
                        active_obj = bpy.context.active_object
                        
                        if active_obj is None or active_obj.type != 'MESH':
                            self.report({'INFO'}, "active object is not Mesh, process aborted")
                            return {'FINISHED'}
                        
                        if bpy.context.mode != 'EDIT':
                                bpy.ops.object.mode_set(mode='EDIT')
                                
                        bm = bmesh.from_edit_mesh(active_obj.data)
                        
                        if(bm is None):
                            self.report({'INFO'}, "bmesh is invalid, process aborted")
                            return {'FINISHED'}
                        
                        for vert in bm.verts:
                            vert.select = False 
                            
                        for edge in bm.edges:
                            edge.select = False
                        
                        for face in bm.faces:
                            face.select = False
                        
                        for vert in bm.verts:
                            if vert.co[0] > 0.0001:
                                    vert.select = True
                        bmesh.update_edit_mesh(active_obj.data)  
                        return {'FINISHED'}    

class Operator_select_x_equal_to_or_smaller_than_zero(bpy.types.Operator):
    bl_idname = "object.select_x_equal_to_or_smaller_than_zero"
    bl_label = "select x <= 0"
    bl_description = "select vertices of x <= 0"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):  
                            # Get the active object
                        active_obj = bpy.context.active_object
                        
                        if active_obj is None or active_obj.type != 'MESH':
                            self.report({'INFO'}, "active object is not Mesh, process aborted")
                            return {'FINISHED'}
                        
                        if bpy.context.mode != 'EDIT':
                                bpy.ops.object.mode_set(mode='EDIT')
                                
                        bm = bmesh.from_edit_mesh(active_obj.data)
                        
                        if(bm is None):
                            self.report({'INFO'}, "bmesh is invalid, process aborted")
                            return {'FINISHED'}
                        
                        for vert in bm.verts:
                            vert.select = False 
                            
                        for edge in bm.edges:
                            edge.select = False
                        
                        for face in bm.faces:
                            face.select = False
                        
                        for vert in bm.verts:
                            if vert.co[0] < 0.0001:
                                    vert.select = True
                        bmesh.update_edit_mesh(active_obj.data)  
                        return {'FINISHED'}    

class Operator_select_x_smaller_than_zero(bpy.types.Operator):
    bl_idname = "object.select_x_smaller_than_zero"
    bl_label = "select x < 0"
    bl_description = "select vertices of x < 0"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):  
                            # Get the active object
                        active_obj = bpy.context.active_object
                        
                        if active_obj is None or active_obj.type != 'MESH':
                            self.report({'INFO'}, "active object is not Mesh, process aborted")
                            return {'FINISHED'}
                        
                        if bpy.context.mode != 'EDIT':
                                bpy.ops.object.mode_set(mode='EDIT')
                                
                        bm = bmesh.from_edit_mesh(active_obj.data)
                        
                        if(bm is None):
                            self.report({'INFO'}, "bmesh is invalid, process aborted")
                            return {'FINISHED'}
                        
                        for vert in bm.verts:
                            vert.select = False 
                            
                        for edge in bm.edges:
                            edge.select = False
                        
                        for face in bm.faces:
                            face.select = False
                        
                        for vert in bm.verts:
                            if vert.co[0] < -0.0001:
                                    vert.select = True
                        bmesh.update_edit_mesh(active_obj.data)  
                        return {'FINISHED'}  
                    
class Menu_select_vertices_by_x_coordinate(bpy.types.Menu):
    bl_idname = "object.menu_vertices_selection"
    bl_label = "Select by x-coordinate"
    bl_description = "Select vertices by x-coordinate."

    def draw(self, context):
        layout = self.layout
        layout.operator(Operator_select_x_equal_to_or_bigger_than_zero.bl_idname, text="Select x >= 0")  
        layout.operator(Operator_select_x_bigger_than_zero.bl_idname, text="Select x > 0")
        layout.operator(Operator_select_x_equal_to_or_smaller_than_zero.bl_idname, text="Select x <= 0")
        layout.operator(Operator_select_x_smaller_than_zero.bl_idname, text="Select x < 0")        
                        
        
def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(Menu_select_vertices_by_x_coordinate.bl_idname)
    
    
def register():
    bpy.utils.register_class(Operator_select_x_equal_to_or_bigger_than_zero)  # Register the operator
    bpy.utils.register_class(Operator_select_x_bigger_than_zero)  # Register the operator 
    bpy.utils.register_class(Operator_select_x_equal_to_or_smaller_than_zero)  # Register the operator  
    bpy.utils.register_class(Operator_select_x_smaller_than_zero)  # Register the operator          
    bpy.utils.register_class(Menu_select_vertices_by_x_coordinate)  # Register the submenu
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_fn) # Add the submenu to the Object menu

def unregister():
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_fn)
    bpy.utils.unregister_class(Menu_select_vertices_by_x_coordinate)
    bpy.utils.unregister_class(Operator_select_x_bigger_than_zero)  # Register the operator   
    bpy.utils.unregister_class(Operator_select_x_equal_to_or_bigger_than_zero)
    bpy.utils.unregister_class(Operator_select_x_smaller_than_zero)  # Register the operator       
    bpy.utils.unregister_class(Operator_select_x_equal_to_or_smaller_than_zero)

if __name__ == "__main__":
    register()             