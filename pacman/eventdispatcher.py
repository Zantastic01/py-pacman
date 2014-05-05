class EventDispatcher:
	events = {}
	def add(self, eventName, listener, methodName):
		listener.eventDispatcher = self

		if eventName not in self.events:
			self.events[eventName] = []

		newListener = {
			'listener': listener,
			'method': methodName
		}

		self.events[eventName].append(newListener)

	def remove(self, eventName, removeListener):
		if eventName not in self.events:
			return;

		for listener in self.events[eventName]:
			if isinstance(listener['listener'], removeListener['listener']):
				if listener['method'] == removeListener['method']:
					self.events[eventName].remove(listener)

	def dispatch(self, eventName, eventSubject):
		if eventName not in self.events:
			return;

		for listener in self.events[eventName]:
			getattr(listener['listener'], listener['method'])(eventSubject);