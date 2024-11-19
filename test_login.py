from playwright.sync_api import Page, expect


def test_login_correct_data(page:Page):
    page.goto('https://app.testomat.io/')
    page.locator('#content-desktop #user_email').fill('dmytro.kulikovskyi@intellias.com')
    page.locator('#content-desktop #user_password').fill('13579_Dimon4IK')
    page.get_by_role('button', name='Sign In').click()
    expect(page.get_by_text('Signed in successfully')).to_be_visible()


def test_login_incorrect_data(page:Page):
    page.goto('https://app.testomat.io/')
    page.locator('#content-desktop #user_email').fill('dmytro.kulikovskyi@intellias.com')
    page.locator('#content-desktop #user_password').fill('incorrect_pass')
    page.get_by_role('button', name='Sign In').click()
    expect(page.locator('#content-desktop .common-flash-info-right')).to_have_text('Invalid Email or password.')