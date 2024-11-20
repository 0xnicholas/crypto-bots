> crypto-bots project breakdown - refer to hummingbot

```
bots (beta)
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


## _renovation project

[] 整合 MEV bots