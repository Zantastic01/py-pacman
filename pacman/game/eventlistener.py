class EventListener:
	listeners = {}
	def add(_self, eventName, listener, methodName):
		if eventName not in _self.listeners:
			_self.listeners[eventName] = []

		newListener = {
			'listener': listener,
			'method': methodName
		}

		_self.listeners[eventName].append(newListener)

	def dispatch(_self, eventName, eventSubject):
		if eventName not in _self.listeners:
			return;

		for listener in _self.listeners[eventName]:
			getattr(listener['listener'], listener['method'])(eventSubject);