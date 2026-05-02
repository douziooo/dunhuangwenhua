# 图片资源文件夹

此文件夹用于存放项目中需要导入使用的图片资源。

## 使用方法

在 Vue 组件中导入图片：

```vue
<script setup>
import imageUrl from '@/assets/images/example.jpg'
</script>

<template>
  <img :src="imageUrl" alt="示例图片" />
</template>
```

## 推荐图片格式

- **JPG/JPEG**: 适合照片和复杂图像
- **PNG**: 适合需要透明背景的图片
- **WebP**: 现代格式，体积更小，推荐使用
- **SVG**: 矢量图，适合图标和简单图形

