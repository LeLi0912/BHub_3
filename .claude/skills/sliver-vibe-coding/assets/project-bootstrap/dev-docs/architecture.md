# Architecture Truth

## 推荐架构

写一个主推荐架构。不要保留多个平级方案。

- 推荐产品形态：
- 推荐技术路线：
- 推荐部署形态：
- 为什么这是主路线：
- 被拒绝路线和原因：

## 技术路线

- 前端框架和理由：
- 设计系统 owner：
- token owner：
- 组件 owner：
- 后端语言/框架和理由：
- 数据库和迁移方式：
- 第三方 SDK/API：
- 是否单运行时：
- 如果跨语言，跨语言真源位置：

## Owner Map

| 概念 | Owner | 不能由谁拥有 | 验证方式 |
| --- | --- | --- | --- |
| 产品边界 |  |  |  |
| 前端路由 |  |  |  |
| 设计 token |  |  |  |
| 业务组件 |  |  |  |
| API 合同 |  |  |  |
| 业务逻辑 |  |  |  |
| 数据库/schema |  |  |  |
| 登录/权限 |  |  |  |
| 第三方接入 |  |  |  |
| 部署/配置 |  |  |  |

## 调用链

```text
用户入口
  -> UI/CLI/API adapter
  -> service/use case
  -> domain/schema/repository
  -> database/provider/runtime
  -> result/report/event
  -> UI/API response
```

## 前端架构

- 设计风格：
- token 文件：
- 主题入口：
- UI/component 基座：
- 页面和业务组件分层：
- 空状态/加载/错误状态规则：
- 禁止混用的样式方式：

## 后端架构

- 后端是否需要：
- 后端负责什么：
- API 合同位置：
- 请求生命周期：
- 统一响应和错误：
- 日志和配置：
- 数据访问：
- 权限和安全：

## 第三方和外部能力

- 官方文档来源：
- SDK/API 版本：
- 鉴权方式：
- webhook/callback：
- sandbox/测试方式：
- quota/rate limit/cost：
- 未验证项：

## 禁止路径

- 禁止 UI 拥有业务真源。
- 禁止 controller/route 写核心业务规则。
- 禁止使用 mock 或本地假数据冒充真实功能。
- 禁止无证据跨语言拆服务。
- 禁止低约束样式工具脱离 token 和组件 owner。
- 禁止私造框架之外的并行目录、状态、生命周期或请求系统。

## 验证方式

- 本地启动命令：
- 构建命令：
- 测试命令：
- UI 截图/点击验证：
- API 请求/响应证据：
- 数据库迁移/回滚证据：
- 安全负例：
- Git checkpoint：
