import unreal

def select_actors_by_name(keyword):
    """
    選取關卡中名稱包含指定關鍵字的 Actor。

    :param keyword: 要搜尋的關鍵字 (string)
    """
    # 1. 取得 Subsystem
    editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # 2. 取得關卡內所有 Actor
    all_actors = editor_actor_subsystem.get_all_level_actors()

    # 3. 將 Text 物件轉成 Python 原生字串並轉小寫
    search_str = str(keyword).lower()

    # 4. 比對 Actor Label（若關鍵字非空才篩選）
    matched_actors = [
        actor for actor in all_actors 
        if search_str and search_str in actor.get_actor_label().lower()
    ]

    # 5. 選取符合條件的 Actor
    editor_actor_subsystem.set_selected_level_actors(matched_actors)

    print(f"已選取 {len(matched_actors)} 個包含 '{search_str}' 的物件")