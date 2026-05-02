# 公共图片资源文件夹

此文件夹用于存放公共静态图片资源，这些图片可以通过 URL 直接访问。

## 使用方法

在 HTML 或 Vue 模板中直接使用路径：

```vue
<template>
  <img src="/images/example.jpg" alt="示例图片" />
</template>
```

或者：

```html
<img src="/images/logo.png" alt="Logo" />
```

## 注意事项

- 放在 `public/images` 中的文件会被直接复制到构建输出的根目录
- 路径以 `/images/` 开头（注意前面的斜杠）
- 适合存放不需要动态导入的静态资源

## 推荐图片格式

- **JPG/JPEG**: 适合照片和复杂图像
- **PNG**: 适合需要透明背景的图片
- **WebP**: 现代格式，体积更小，推荐使用
- **SVG**: 矢量图，适合图标和简单图形

