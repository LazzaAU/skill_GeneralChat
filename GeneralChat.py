from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class GeneralChat(AliceSkill):
	"""
	Author: LazzaAU
	Description: Adds some more every day chat to alice
	"""


	@IntentHandler('sayGreeting')
	def saygreetingIntent(self, session: DialogSession):
		self.endDialog(sessionId=session.sessionId, text=self.randomTalk('respondHello'), siteId=session.siteId)

	@IntentHandler('sayFeelings')
	def sayfeelingIntent(self, session: DialogSession):
		self.endDialog(sessionId=session.sessionId, text=self.randomTalk('respondFeeling'), siteId=session.siteId)

