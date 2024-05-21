import time
from pydbus import SystemBus
from gi.repository import GLib

def register_hid_profile(adapter_id, target_address):
    bus = SystemBus()
    bluez = bus.get("org.bluez", "/org/bluez")

    manager = bluez["org.bluez.ProfileManager1"]

    profile_path = "/test/hidprofile"
    opts = {
        "ServiceRecord": """
        <record>
            <attribute id="0x0001">
                <sequence>
                    <uuid value="0x1124"/>
                </sequence>
            </attribute>
        </record>
        """,
        "Role": "server",
        "RequireAuthentication": True,
        "RequireAuthorization": True,
        "AutoConnect": True,
        "Service": "human interface device",
        "Name": "HID",
        "PSM": 17,
        "Channel": 1,
        "Version": 0x0100,
        "Description": "Termux HID",
    }

    manager.RegisterProfile(profile_path, "00001124-0000-1000-8000-00805f9b34fb", opts)

    def unregister():
        manager.UnregisterProfile(profile_path)

    loop = GLib.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()
        unregister()

def agent_loop(agent_path):
    bus = SystemBus()
    bluez = bus.get("org.bluez", "/org/bluez")

    agent_manager = bluez["org.bluez.AgentManager1"]
    agent_manager.RegisterAgent(agent_path, "NoInputNoOutput")
    agent_manager.RequestDefaultAgent(agent_path)

    loop = GLib.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()
        agent_manager.UnregisterAgent(agent_path) 
