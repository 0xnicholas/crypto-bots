# Crypto bots
> frameworks for crypto [trader/quant/miner/maker] -refer to hummingbot

## Strategy Architecture


## Core

## Client/Cmd
> only support cmd.


## Connectors
连接器标准
- spot：基于 WebSocket 的连接器，可连接交易所提供的基于现货订单簿的市场，交易所可以CEX，也可以是DEX。
- perp：基于 WebSocket 的连接器，用于连接交易所提供的基于永久期货订单簿的市场，可以是集中式（CEX）或分散式（DEX）。
- gateway：基于 REST 的连接器，用于连接区块链网络及其AMM和 CLOB DEX, Gateway 连接器可以是连接器，也可以是链。

### API Requirements
具有REST API的交易所必须提供的endpoint：
- 获取交易规则 
- 检查服务器状态 
- 获取活跃订单 
- 创建新订单 
- 获取当前账户余额
- 每个endpoint的应用速率限制和每个IP/连接全局限制的文档

如果 REST API 提供以下内容，则很有用，但可以在没有它们的情况下构建连接器：
- 获取活跃交易对列表（有时称为“tokens info”）

具有 WebSocket API 的交易所必须提供：
- Pulbic orders通道 
- Public trades通道 
- Private orders更新通道 
- Private trades 事件通道 
- 记录每个订阅的速率限制和每个 IP/连接的全局限制

如果 Websocket API 还提供以下内容，那将会很有用，但是可以在没有它们的情况下构建连接器：
- Private balance事件通道（如果没有，则必须配置连接器以根据连接器活动估算余额）
- 交易事件，包括有关每笔交易收取的费用的详细信息（如果没有，则连接器必须估算费用）

perp连接器的其他要求：
- 用于检查头寸的REST API endpoint 
- 用于配置杠杆的REST API endpoint 

## project breakdown (non opensource)

```
crypto-bots (beta)
│
├── cli					# CLI related files
│
├── connector				# connectors to individual exchanges
│   ├── derivative			# derivative connectors
│   ├── exchange	 		# spot exchanges
│   ├── gateway				# gateway connectors
│   ├── other				# misc connectors	
│   └── utilities			# helper functions / libraries that support connector functions
│
├── core
│   ├── api_throttler			# api throttling mechanism
│   ├── cpp				# high performance data types written in .cpp
│   ├── data_type			# key data
│   ├── event				# defined events and event-tracking related files								
│   ├── gateway				# gateway related components
│   ├── management			# management related functionality such as console and diagnostic tools
│   ├── mock_api			# mock implementation of APIs for testing
│   ├── rate_oracle			# manages exchange rates from different sources 
│   ├── utils				# helper functions and bot plugins		
│   └── web_assistant			# web related functionalities
│
├── price_feed				# price feeds such as CoinCap
│
├── logger				# handles logging functionality
│
├── data_model				# data models for managing DB migrations and market data structures
│
├── notifier				# connectors to services that sends notifications such as Wechat or Telegram
│
├── remote_iface			# remote interface for external services like MQTT
│
├── strategy			# smart components like controllers, executors and frameworks for strategy implementation
│   ├── controllers			# controllers scripts for various trading strategy or algorithm				
│   ├── executors			# various executors 
│   ├── backtesting 		# base frameworks for strategies including backtesting and base classes
│   └── utils				# utility scripts and modules that support smart components
│
├── templates				# templates for config files: general, strategy, and logging
│
└── user				# handles user-specific data like balances across exchanges
```


## _memo

- [x] 整合 MEV bots
- [x] ML helper