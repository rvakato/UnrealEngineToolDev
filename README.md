# UnrealEngineToolDev

*(目前使用 UE5.5 開發 / Currently developed with UE5.5)*

---

## 專案介紹 (Project Introduction)

**中**：  
UnrealEngineToolDev 是我在開發 Unreal Engine 遊戲與應用時所使用的工具集合。此專案會持續更新並新增各種自製的 UE 工具，方便快速整合與分享。以下列出目前包含的工具，並隨時補充新的範例與插件。

**EN**:  
UnrealEngineToolDev is a collection of custom tools I use when developing with Unreal Engine. This repository is continuously updated with new UE tools, making it easy to integrate and share. Below are the tools currently included, with more to be added over time.

---

## 工具一覽 (Tools Overview)

- **BP_SingleAssetVariation**  
  - **中**：示範如何在指定位置列表中隨機生成不同的 Static Mesh，並套用隨機旋轉與縮放。  
  - **EN**: Demonstrates how to randomly spawn different Static Meshes at specified target locations, applying random rotation and scale.

---

## BP_SingleAssetVariation

### 簡介 (Introduction)

**中**：  
`BP_SingleAssetVariation` 範例示範了如何在指定目標位置列表中隨機生成不同的 Static Mesh，並對每個物件套用隨機旋轉與縮放。透過設定 Mesh Variations、Rotation Range 和 Scale Range，即可快速在場景中產生多樣化佈局。教學影片帶你一步步從零開始構建此工具：  
https://www.youtube.com/watch?v=DlrPtW1X0us
![Thumbnail](https://github.com/user-attachments/assets/de876d0b-226a-4db8-bb67-df335fa8ccd8)

**EN**:  
`BP_SingleAssetVariation` is an example that demonstrates how to randomly spawn different Static Meshes at specified target locations, applying random rotation and scale to each instance. By configuring Mesh Variations, Rotation Range, and Scale Range, you can quickly generate varied layouts within your level. The tutorial video walks you through building this tool from scratch:  
https://www.youtube.com/watch?v=DlrPtW1X0us
![Thumbnail](https://github.com/user-attachments/assets/fd51c6aa-25fe-44f0-a671-596d54edc58b)


### 使用方式 (Usage)

- **中**：  
  1. 在 Content Browser 或使用完整路徑欄，找到並拖曳以下資源到場景中：  
     ```  
     /Script/Engine.Blueprint'/Game/RvToolKit/Blueprint/BP_SingleAssetVariation.BP_SingleAssetVariation'  
     ```  
     ![步驟1：拖曳 Blueprint](https://github.com/user-attachments/assets/bacddffd-b713-43d3-af1b-137f7ad19fd5)  
  2. 在 Details 面板中，於 **Mesh Variations** 欄位新增想要隨機切換的 Static Mesh。  
     ![步驟2：新增 Static Mesh Variations](https://github.com/user-attachments/assets/a2dfcbb2-cd98-4361-b383-442d4c68362b)  
  3. 設定 **Rotation Range**（如 0–360）與 **Scale Range**（如 0.8–1.2），以控制隨機旋轉與縮放範圍。  
     ![步驟3：設定 Rotation & Scale 範圍](https://github.com/user-attachments/assets/542ab6df-0650-4ddf-9efc-03c35d3e9629)  
  4. 修改參數後，Blueprint 會在編輯器中自動更新並顯示結果，無需執行遊戲或額外操作。  

- **EN**:  
  1. In the Content Browser or by using the path bar, locate and drag the following asset into your level:  
     ```  
     /Script/Engine.Blueprint'/Game/RvToolKit/Blueprint/BP_SingleAssetVariation.BP_SingleAssetVariation'  
     ```  
     ![Step 1: Drag Blueprint into Level](https://github.com/user-attachments/assets/bacddffd-b713-43d3-af1b-137f7ad19fd5)  
  2. In the Details panel, add the Static Meshes you want randomized to the **Mesh Variations** array.  
     ![Step 2: Add Static Mesh Variations](https://github.com/user-attachments/assets/a2dfcbb2-cd98-4361-b383-442d4c68362b)  
  3. Configure the **Rotation Range** (e.g., 0–360) and **Scale Range** (e.g., 0.8–1.2) to control the random rotation and scaling.  
     ![Step 3: Configure Rotation & Scale Ranges](https://github.com/user-attachments/assets/542ab6df-0650-4ddf-9efc-03c35d3e9629)  
  4. After adjusting parameters, the Blueprint updates automatically in the editor—no need to run the game or perform additional steps.  

---

##### 感謝使用與觀看教學影片！  
##### Thank you for using this tool and watching the tutorial!  
