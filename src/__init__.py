from ovos_utils import classproperty
from ovos_utils.process_utils import RuntimeRequirements
# from ovos_workshop.intents import IntentBuilder
# from ovos_workshop.decorators import intent_handler
# from ovos_workshop.intents import IntentHandler # Uncomment to use Adapt intents
from ovos_workshop.skills import OVOSSkill

import sys
from os.path import expanduser
home = expanduser("~")
sys.path.append(home)
from SMS import SIM7600X

# Optional - if you want to populate settings.json with default values, do so here
DEFAULT_SETTINGS = {
    "setting1": True,
    "setting2": 50,
    "setting3": "test"
}

class TextEmergencySkill(OVOSSkill):
    def __init__(self, *args, skill_id=None, bus=None, **kwargs):
        super().__init__(*args, skill_id=skill_id, bus=bus, **kwargs)
        self.learning = True

    def initialize(self):
        self.settings.merge(DEFAULT_SETTINGS, new_only=True)
        self.add_event('recognizer_loop:hotword', self.handle_text_help)
        self.add_event('text.emergency', self.handle_text_help)
        phone = SIM7600X() # instance of cellular module

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(
            internet_before_load=False,
            network_before_load=False,
            gui_before_load=False,
            requires_internet=False,
            requires_network=False,
            requires_gui=False,
            no_internet_fallback=True,
            no_network_fallback=True,
            no_gui_fallback=True,
        )

    @property
    def my_setting(self):
        """Dynamically get the my_setting from the skill settings file.
        If it doesn't exist, return the default value.
        This will reflect live changes to settings.json files (local or from backend)
        """
        return self.settings.get("my_setting", "default_value")

    def handle_text_help(self, message):
        self.speak("Contacting emergency services right now")
        self.speak("This is from skill r 2 arck text skill")
        #phone.send_short_message("Send help to CSULB ASAP")

    def stop(self):
        return
