// 页面滚动效果
window.addEventListener('scroll', function() {
    const nav = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        nav.classList.add('navbar-scrolled');
    } else {
        nav.classList.remove('navbar-scrolled');
    }
});

// 移动端菜单切换
document.addEventListener('DOMContentLoaded', function() {
    // 移动端菜单切换
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuButton) {
        mobileMenuButton.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // 关闭闪现消息
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        const closeButton = message.querySelector('.close-button');
        if (closeButton) {
            closeButton.addEventListener('click', () => {
                message.remove();
            });
        }
        // 5秒后自动消失
        setTimeout(() => {
            message.remove();
        }, 5000);
    });
});