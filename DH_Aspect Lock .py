bl_info = {
    "name": "Auto Aspect Lock (解像度比率固定)",
    "author": "DaHi64",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Output Properties > Format",
    "description": "解像度XまたはYを変更した際、アスペクト比を維持して自動追従させます。",
    "warning": "",
    "doc_url": "",
    "category": "Render",
}

import bpy
from bpy.app.handlers import persistent

# 内部的な無限ループを防ぐためのフラグと、前回の値を記憶する変数
class AspectLockItem:
    is_updating = False
    last_x = 1920
    last_y = 1080
    aspect_ratio = 1920 / 1080

# アドオン有効化時の初期値を設定
def init_ratio(scene):
    AspectLockItem.last_x = scene.render.resolution_x
    AspectLockItem.last_y = scene.render.resolution_y
    if AspectLockItem.last_y != 0:
        AspectLockItem.aspect_ratio = AspectLockItem.last_x / AspectLockItem.last_y

@persistent
def aspect_lock_handler(scene):
    # ロック機能がOFF、またはスクリプト自身による変更時は処理をスキップ
    if not getattr(scene, "use_aspect_lock", False) or AspectLockItem.is_updating:
        return

    current_x = scene.render.resolution_x
    current_y = scene.render.resolution_y

    # Xが変更された場合
    if current_x != AspectLockItem.last_x:
        AspectLockItem.is_updating = True
        new_y = int(current_x / AspectLockItem.aspect_ratio)
        scene.render.resolution_y = max(1, new_y) # 1ピクセル未満にならないように
        AspectLockItem.last_x = current_x
        AspectLockItem.last_y = scene.render.resolution_y
        AspectLockItem.is_updating = False

    # Yが変更された場合
    elif current_y != AspectLockItem.last_y:
        AspectLockItem.is_updating = True
        new_x = int(current_y * AspectLockItem.aspect_ratio)
        scene.render.resolution_x = max(1, new_x)
        AspectLockItem.last_x = scene.render.resolution_x
        AspectLockItem.last_y = current_y
        AspectLockItem.is_updating = False

# 解像度比率をその場で再取得（ロックON時や手動リセット用）
def update_lock_toggle(self, context):
    if self.use_aspect_lock:
        init_ratio(context.scene)

# UIを「出力プロパティ」の「フォーマット」パネルに追加
def draw_aspect_lock_ui(self, context):
    layout = self.layout
    scene = context.scene
    
    # 標準の解像度設定のすぐ下、あるいは隣に配置しやすいように
    row = layout.row(align=True)
    row.prop(scene, "use_aspect_lock", text="解像度比率を固定", icon='LOCKED' if scene.use_aspect_lock else 'UNLOCKED')


def register():
    bpy.types.Scene.use_aspect_lock = bpy.props.BoolProperty(
        name="Use Aspect Lock",
        description="解像度XとYの比率を固定します",
        default=False,
        update=update_lock_toggle
    )
    
    # 出力プロパティ（RENDER_PT_format）のUIに組み込み
    bpy.types.RENDER_PT_format.append(draw_aspect_lock_ui)
    
    # 毎フレーム/プロパティ更新時に実行されるハンドラーに登録
    if aspect_lock_handler not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(aspect_lock_handler)

def unregister():
    if aspect_lock_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(aspect_lock_handler)
        
    bpy.types.RENDER_PT_format.remove(draw_aspect_lock_ui)
    del bpy.types.Scene.use_aspect_lock

if __name__ == "__main__":
    register()