import pyautogui

from roundup.roundup_mission import RoundupMission

roundup = RoundupMission()

# roundup.start_app()
# roundup.trigger_image_recognition('images/support.png', 944, 513)
# roundup.trigger_image_recognition('images/shinobi_menu.png', 1420, 453)
# roundup.mouse_click_and_slide(611, 925, 1112, 925)
# roundup.trigger_image_recognition('images/roundup_mission.png', 1023, 596)
roundup.trigger_image_recognition('images/solo_battle.png', 943, 868)

pyautogui.sleep(2)
pyautogui.click(595, 655)

while True:
    roundup.trigger_image_recognition_and_click_on_it('images/next.png')
    roundup.trigger_image_recognition_and_click_on_it('images/ok.png')
    roundup.trigger_image_recognition('images/result.png', 941, 868)

    for i in range(8):
        pyautogui.sleep(2)
        pyautogui.click(941, 868)
