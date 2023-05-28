import time

import pyautogui
from surprise_attack.surprise_attack_mission import SurpriseAttackMission

sam = SurpriseAttackMission()

# sam.start_app()
# sam.trigger_image_recognition('images/support.png', 944, 513)
# sam.trigger_image_recognition('images/shinobi_menu.png', 1420, 453)
# sam.trigger_image_recognition_and_click_on_it('images/surprise_attack_mission.png')
# sam.trigger_image_recognition_and_click_on_it('images/unseal.png')
#
# for _ in range(4):
#     pyautogui.click(1273, 610)
#     pyautogui.sleep(0.5)

while True:
    sam.trigger_image_recognition_and_click_on_it('images/mirage_master.png')
    sam.trigger_image_recognition_and_click_on_it('images/yes.png')
    sam.trigger_image_recognition_and_click_on_it('images/skip.png')
    sam.trigger_image_recognition_and_click_on_it('images/ok_sam.png')

    duration = 160
    start_time = time.time()

    while time.time() - start_time < duration:
        sam.trigger_jutsu_image_recognition_and_click_on_it('images/sasuke_tfs_ultimate.png')
        sam.trigger_jutsu_image_recognition_and_click_on_it('images/sasuke_tfs_old_lb.png')
        sam.trigger_jutsu_image_recognition_and_click_on_it('images/sasuke_tfs_new_4_star.png')
        sam.trigger_jutsu_image_recognition_and_click_on_it('images/sasuke_tfs_new_lb.png')

    pyautogui.sleep(8)

    for i in range(12):
        pyautogui.sleep(2)
        pyautogui.click(941, 868)
