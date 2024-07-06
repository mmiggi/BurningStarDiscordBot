__package__ = "views"

import nextcord
from nextcord import Embed

from views.EventView import EventView

class SigneupCloseView(EventView):
    def __init__(self, discord_timestamp, event_day, singups, event_type, discription, roles, restore_code=None):
        super().__init__(discord_timestamp, event_day, singups, event_type, discription)
        self.roles = roles
        self.embeded = Embed(title = "Event Signup for " + event_day + " is closed!")
        self.restore_code = restore_code

    def embeded_create(self):
        self.embeded.colour = self.get_colour()
        self.embeded.set_image("https://cdn.discordapp.com/attachments/827147397184487456/1211101174195949628/closed.jpg?ex=65ecf8dd&is=65da83dd&hm=fecf0cba5963e4d35200c0440c78a13fd481fa6968ad0040c920e842045e2296&")
        self.embeded.add_field(name = "Your local time: ", value = self.timestamp, inline=False)
        self.embeded.add_field(name = "Event Type", value = self.event_type, inline=False)
        if self.discription != "":
            self.embeded.add_field(name = "Event details", value = self.discription, inline=False)

        self.embeded.add_field(name = "+++++++++++++++++++++++++++++++++++++++++++++++++", value=" ", inline=False)
        index = 0
        first = False
        for singup in self.singups:
            
            
            user_string = self.generate_user_string(singup)
            self.embeded.add_field(name = self.roles[index] + " ["+ str(len(singup))+ "]", value = user_string, inline=first)
            index += 1

            if index > 0:
                first = False

        self.embeded.add_field(name = "+++++++++++++++++++++++++++++++++++++++++++++++++", value=" ", inline=False)
        self.embeded.add_field(name = "If you still like to join DM: ", value = "Firedragon, Lia or the Coordinator", inline=False)
        self.embeded.add_field(name = "Restorecode: ", value = self.restore_code, inline=False)

        return self.embeded
    

    def generate_user_string(self, userlist):
        user_string = ""
        for user in userlist:
            user_string += str(user) + "\n"
        user_string += "------------\n"
        return user_string
        