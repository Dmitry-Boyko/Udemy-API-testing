// Here's a basic WebdriverIO test example for a login scenario using the Mocha framework and sync mode:

describe('Login Page', () => {
    it('should login with valid credentials', async () => {
        await browser.url('https://example.com/login');

        const usernameInput = await $('#username');
        const passwordInput = await $('#password');
        const loginButton = await $('#login-button');

        await usernameInput.setValue('valid_user');
        await passwordInput.setValue('valid_password');
        await loginButton.click();

        const logoutButton = await $('#logout-button');
        await expect(logoutButton).toBeDisplayed();
    });
});

//This script:
//- Navigates to the login page
//- Enters valid credentials
//- Clicks the login button
//- Verifies that the logout button appears, indicating a successful login


