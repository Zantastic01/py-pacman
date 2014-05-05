class EventDispatcher:
	listeners = {}
	def add(self, eventName, listener, methodName):
		listener.eventDispatcher = self

		if eventName not in self.listeners:
			self.listeners[eventName] = []

		newListener = {
			'listener': listener,
			'method': methodName
		}

		self.listeners[eventName].append(newListener)

	def dispatch(self, eventName, eventSubject):
		if eventName not in self.listeners:
			return;

		for listener in self.listeners[eventName]:
			getattr(listener['listener'], listener['method'])(eventSubject);