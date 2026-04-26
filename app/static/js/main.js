/**
 * 出国（境）学习交流项目展示系统 - 主脚本
 * 包含导航交互、滚动动画、手风琴等通用功能
 */

document.addEventListener('DOMContentLoaded', function () {

    // ============================================
    // 导航栏滚动效果
    // ============================================
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // ============================================
    // 移动端菜单切换
    // ============================================
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            navMenu.classList.toggle('active');
            // 汉堡菜单动画
            navToggle.classList.toggle('active');
        });

        // 点击菜单项关闭菜单
        navMenu.querySelectorAll('.nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            });
        });

        // 移动端下拉菜单
        document.querySelectorAll('.nav-dropdown > .nav-link').forEach(function (dropdownLink) {
            dropdownLink.addEventListener('click', function (e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    this.parentElement.classList.toggle('open');
                }
            });
        });
    }

    // ============================================
    // 滚动显示动画 (Intersection Observer)
    // ============================================
    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(function (el) {
            observer.observe(el);
        });
    } else {
        // 降级处理：直接显示
        revealElements.forEach(function (el) {
            el.classList.add('visible');
        });
    }

    // ============================================
    // 手风琴组件
    // ============================================
    document.querySelectorAll('.accordion-header').forEach(function (header) {
        header.addEventListener('click', function () {
            const item = this.parentElement;
            const content = item.querySelector('.accordion-content');
            const isActive = item.classList.contains('active');

            // 关闭所有其他项
            document.querySelectorAll('.accordion-item').forEach(function (otherItem) {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    var otherContent = otherItem.querySelector('.accordion-content');
                    if (otherContent) {
                        otherContent.style.maxHeight = null;
                    }
                }
            });

            // 切换当前项
            if (isActive) {
                item.classList.remove('active');
                content.style.maxHeight = null;
            } else {
                item.classList.add('active');
                content.style.maxHeight = content.scrollHeight + 'px';
            }
        });
    });

    // ============================================
    // 平滑滚动到锚点
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var targetId = this.getAttribute('href');
            if (targetId === '#') return;

            var target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                var offsetTop = target.getBoundingClientRect().top + window.pageYOffset - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============================================
    // 数字递增动画
    // ============================================
    var statNumbers = document.querySelectorAll('.stat-number[data-count]');
    if (statNumbers.length > 0 && 'IntersectionObserver' in window) {
        var statsObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(function (el) {
            statsObserver.observe(el);
        });
    }

    /**
     * 数字递增动画
     * @param {HTMLElement} element - 目标元素
     */
    function animateCounter(element) {
        var target = parseInt(element.getAttribute('data-count'), 10);
        var current = 0;
        var increment = Math.ceil(target / 40);
        var duration = 1500; // 总时长(ms)
        var stepTime = duration / (target / increment);

        var timer = setInterval(function () {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = current + '+';
        }, stepTime);
    }

    // ============================================
    // 页面加载完成提示
    // ============================================
    console.log('出国交流项目展示系统已加载完成');
});
