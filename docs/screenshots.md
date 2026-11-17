# README 展示图

两张展示图由用户提供的界面截图经内置 imagegen 局部编辑和裁切得到。它们用于介绍功能，不作为原生入口图标状态或实时角标的验收证据。

- `images/project-overview.png`：保留公开项目名称，其余项目改为编号；所有本机路径替换为隐藏提示。
- `images/linked-todos.png`：私人待办标题和关联项目替换为示例；保留优先级、截止日期与操作控件。
- 两张图均移除宿主侧栏、个人头像和聊天输入区。原始截图不入库。
- 发布前人工查看两张成图，并用 OCR 检查原截图中的英文私有项目名和路径片段；PNG 不包含文本或 EXIF 元数据。

## 总览图编辑提示词

```text
Use case: precise-object-edit / text-localization.
Edit target: the attached real Project Pulse project-overview screenshot. This is a privacy redaction for a public GitHub README, not a redesign.
Crop to the plugin content panel: remove the macOS title bar, entire left host navigation (including personal avatar), and the bottom blank area / floating composer. Keep the complete plugin top navigation, summary row, filters, search, add-todo button, and all 22 project cards. Target landscape framing about 2.35:1, crisp high-resolution screenshot.
Privacy edits are mandatory: erase EVERY filesystem path line in ALL 22 cards, including the first card. Replace each path with the neutral text "路径已隐藏". No original path letters may remain. Erase ALL private card titles. Keep only the first public title "codex-project-pulse"; replace the other 21 titles in reading order with "Project 02" through "Project 22". Do not retain any original project names except codex-project-pulse.
Preserve precisely all other visible UI text, counts, icons, borders, spacing, 6-column grid with 4 cards on the last row, current status colors (first card pale purple; third card pale amber; all others white), and top navigation highlighting. All existing labels stay Chinese. Do not invent features, change numeric counts, add unread dots, redesign the logo, add headings, shadows or annotations. Keep the original white/neutral visual style. Output one clean, tightly cropped, privacy-safe screenshot with readable UI text.
```

## 待办图编辑提示词

```text
Use case: precise-object-edit / text-localization.
Edit target: the attached real Project Pulse "我的待办" screenshot. Prepare a privacy-safe image for its public GitHub README. This is a local text redaction and crop, not a redesign.
Crop away the macOS title bar, entire left host navigation including personal avatar, bottom floating composer, and most of the empty white lower page. Preserve the entire plugin top navigation, summary row, filter row, search, add-todo and export buttons, and the complete single todo row with its checkbox and edit control. Produce a crisp wide landscape crop around 3:1 with no decorative frame, no extra headings.
Privacy: completely erase the existing private todo title and replace it with exactly "检查发布清单". Completely erase the private project name below it and replace it with exactly "Project 03", matching the anonymized project overview. Preserve the adjacent "优先" badge and "11-18" due date. No original private title or project name or avatar may remain.
All other original UI labels and numeric counts must remain unchanged. Keep the "我的待办" tab selected and the "未完成" filter selected. Preserve white background, neutral borders, black controls, typography, original proportions, icons and alignment. Do not invent additional todos, statuses, native badges, UI controls or features. Make only the specified privacy replacements and tighter framing.
```

