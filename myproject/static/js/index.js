const toggleButton = document.getElementById('toggleForm');
const loginForm = document.querySelector('.login-form');
const registrationForm = document.querySelector('.registration-form');
const formPanel = document.querySelector('.form-panel');
const registrationPanel = document.querySelector('.registration-panel');
const panelTitle = document.querySelector('.panel-title');
const subTitle = document.querySelector('.subTitle');
let isRegistrationMode = false;

function toggleLoginAndRegistration() {
    if (isRegistrationMode) {
        registrationPanel.style.left = '640px';
        formPanel.style.left = '0';
        toggleButton.innerText = '注册';
        panelTitle.innerText = '还未注册？';
        subTitle.innerText = '立即注册，发现大量机会！';
        setTimeout(() => {
            loginForm.style.display = 'flex';
            registrationForm.style.display = 'none';
        }, 300);
    } else {
        registrationPanel.style.left = '0';
        formPanel.style.left = '260px';
        toggleButton.innerText = '登录';
        panelTitle.innerText = '已有帐号？';
        subTitle.innerText = '有帐号就登录吧，好久不见了！';
        setTimeout(() => {
            loginForm.style.display = 'none';
            registrationForm.style.display = 'flex';
        }, 300);
    }
    isRegistrationMode = !isRegistrationMode;
}

toggleButton.addEventListener('click', toggleLoginAndRegistration);

// 注册按钮跳转到注册页面，登录按钮跳转到登录页面函数
function redirectToRegisterPage() {
    window.location.href = '/myapp/register/';
}
