# feishu-integration.md - 飞书集成知识

飞书平台的集成配置、使用经验和最佳实践。

---

## 当前配置

### Webhook配置

**目的**：让飞书能向OpenClaw发送消息和事件

**配置方式**：
- 使用ngrok暴露本地OpenClaw
- 公网地址：`https://griffin-subchorioidal-contritely.ngrok-free.dev`
- 转发到：`localhost:3000`（OpenClaw webhook端口）
- Webhook路径：`/feishu/events`

**已知问题**：
- ngrok在国内访问不稳定
- 连接频繁断开
- 免费版有连接限制

**替代方案**：
1. 使用国内内网穿透服务（cpolar、frp）
2. 使用云服务器部署OpenClaw
3. 使用飞书官方云托管

---

### 权限配置

**配置日期**：2026-02-25

**已配置权限**：
- 消息发送权限
- 消息撤回权限
- 资源访问权限
- 其他多项权限（具体列表见飞书开放平台）

**权限管理**：
- 飞书开放平台：https://open.feishu.cn
- 应用管理：查看和配置权限

---

## OpenClaw飞书集成

### 支持的功能

**消息收发**：
- ✅ 接收飞书消息
- ✅ 发送文本消息
- ✅ 发送富文本消息
- ✅ 发送交互式卡片（需配置）

**事件处理**：
- ✅ 消息事件
- ✅ 其他飞书事件

**权限控制**：
- ✅ 通过OpenClaw配置文件管理

### 配置文件

**位置**：OpenClaw配置目录
**内容**：
- 飞书App ID
- 飞书App Secret
- Webhook地址
- 权限配置

---

## 使用经验

### 消息格式

**文本消息**：
```json
{
  "msg_type": "text",
  "content": {
    "text": "消息内容"
  }
}
```

**富文本消息**：
```json
{
  "msg_type": "post",
  "content": {
    "post": {
      "zh_cn": {
        "title": "标题",
        "content": [
          [{"tag": "text", "text": "内容"}]
        ]
      }
    }
  }
}
```

**交互式卡片**：
- 需要配置 `feishu.capabilities.inlineButtons`
- 支持：`"dm"` | `"group"` | `"all"` | `"allowlist"`

### 最佳实践

**1. 错误处理**
```javascript
try {
  await feishu.sendMessage(message);
} catch (error) {
  console.error('飞书消息发送失败:', error);
}
```

**2. 权限检查**
- 发送前检查是否有权限
- 权限不足时给出明确提示

**3. 消息格式**
- 飞书不支持markdown表格
- 使用列表或卡片代替
- 注意中英文混排

---

## 常见问题

### Webhook无法接收事件

**症状**：
- 飞书发送消息，OpenClaw无响应
- ngrok显示连接断开

**可能原因**：
1. ngrok连接断开
2. Webhook地址配置错误
3. 飞书权限未配置

**解决方案**：
1. 检查ngrok状态
2. 验证Webhook地址
3. 检查飞书开放平台权限配置

### 消息发送失败

**症状**：
- OpenClaw尝试发送消息失败
- 飞书提示权限不足

**可能原因**：
1. 缺少消息发送权限
2. 用户/群聊ID错误
3. 消息格式不正确

**解决方案**：
1. 检查飞书开放平台权限
2. 验证接收者ID
3. 检查消息格式

### 中文乱码

**症状**：
- 发送的中文显示为乱码

**可能原因**：
- 编码问题

**解决方案**：
- 确保使用UTF-8编码
- 检查消息内容的编码

---

## API参考

### OpenClaw飞书工具

**可用工具**：
- `feishu_doc` - 文档操作
- `feishu_drive` - 云盘操作
- `feishu_wiki` - 知识库操作
- `feishu_bitable_*` - 多维表格操作
- `message` - 消息发送（支持飞书）

### 使用示例

**读取飞书文档**：
```
feishu_doc(action="read", doc_token="xxx")
```

**发送消息**：
```
message(
  action="send",
  channel="feishu",
  target="user:ou_xxx",
  message="消息内容"
)
```

---

## 安全注意事项

### 敏感信息

**不要公开**：
- 飞书App Secret
- Webhook地址（如果暴露在公网）
- 用户Open ID

**已配置保护**：
- `.claudeignore` - 防止AI读取敏感配置
- `.gitignore` - 防止敏感信息提交到Git

### Webhook安全

**验证请求来源**：
- 飞书会发送签名
- 验证签名确保请求来自飞书

**防止重放攻击**：
- 检查时间戳
- 拒绝过期的请求

---

## 待优化

- [ ] 替换ngrok为稳定方案
- [ ] 配置交互式卡片权限
- [ ] 完善错误处理
- [ ] 添加消息模板
- [ ] 优化Webhook安全验证

---

## 相关链接

- 飞书开放平台：https://open.feishu.cn
- OpenClaw文档：https://docs.openclaw.ai
- ngrok：https://ngrok.com

---

_最后更新：2026-03-05_
_配置状态：基础功能可用，ngrok不稳定_
