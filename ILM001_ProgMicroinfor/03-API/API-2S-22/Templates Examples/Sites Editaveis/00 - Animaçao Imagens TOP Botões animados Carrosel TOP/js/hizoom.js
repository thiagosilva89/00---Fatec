(function($) {
    // 主逻辑封装在函数里
    // 主要利用了函数的局部作用域解决同一页面调用多次插件造成的作用域混乱的问题
    var start = function(el,options) {
        var magnifier = null; //当前放大镜DOM
        var bigImageDOM = null; // 当前大图容器DOM
        var leftDistance = undefined; // 鼠标距离容器左边的距离
        var topDistance = undefined;
        var config = {
            width: 400,
            position: 'right',
            background: '#fff',
            opacity: 0.7, // 放大镜透明度
            distance: 20 // 被放大区域距离原区域的距离
        };

        // 放大镜没有触碰到容器边距 ? true : false
        var notTouchBorder = function() {
            if (
                leftDistance >= config.width / 4 &&
                leftDistance <= 3 * config.width / 4 &&
                topDistance >= config.width / 4 &&
                topDistance <= 3 * config.width / 4
            ) {
                return true;
            }
            return false;
        };
        // 创建所需要的DOM
        var prepareDOM = function(dom) {
            // 遍历每个放大镜div容器
            dom.each(function() {
                // 克隆图片DOM
                var img = $(this)
                    .find('img')
                    .clone();
                // 插入small,big两个div
                $(this).append(
                    $(
                        '<div class="small"><div class="magnifier"></div></div></div><div class="big"></div>'
                    )
                );
                // 两个容器div插入图片
                $(this)
                    .children('div')
                    .append(img);
                // 删除第一张图片
                $(this)
                    .find('img')
                    .first()
                    .remove();
            });
        };

        // 给放大镜small区域div绑定鼠标移动事件
        var bindListener = function(dom) {
            dom.each(function() {
                $(this)
                    .find('.small')
                    .mouseenter(function(e) {
                        // 鼠标进入
                        enterLogic($(this), e);
                    })
                    .mousemove(function(e) {
                        // 鼠标内部移动
                        var offset = $(this).offset();
                        var scrollTop =
                            document.body.scrollTop ||
                            document.documentElement.scrollTop;
                        var scrollLeft =
                            document.body.scrollLeft ||
                            document.documentElement.scrollLeft;

                        leftDistance = e.clientX - (offset.left - scrollLeft);
                        topDistance = e.clientY - (offset.top - scrollTop);

                        mainLogic();
                    })
                    .mouseleave(function(e) {
                        // 鼠标移除
                        $(this)
                            .siblings('.big')
                            .hide();
                        magnifier.hide();
                        // 鼠标离开，初始化DOM变量

                        resetVar();
                    });
            });
        };

        // 鼠标进入容器的瞬间的逻辑
        var enterLogic = function($this, event) {
            var offset = $this.offset();
            var scrollTop =
                document.body.scrollTop || document.documentElement.scrollTop;
            var scrollLeft =
                document.body.scrollLeft || document.documentElement.scrollLeft;

            leftDistance = event.clientX - (offset.left - scrollLeft);
            topDistance = event.clientY - (offset.top - scrollLeft);

            magnifier = $this.find('.magnifier');
            var big = $this.siblings('.big');
            bigImageDOM = big.find('img');
            // 左上（config.width / 4px正方形内）
            if (
                leftDistance <= config.width / 4 &&
                topDistance <= config.width / 4
            ) {
                magnifier.css({
                    top: 0,
                    left: 0
                });
                bigImageDOM.css({
                    top: 0,
                    left: 0
                });
                // 左下
            } else if (
                leftDistance <= config.width / 4 &&
                topDistance >= 3 * config.width / 4
            ) {
                magnifier.css({
                    top: config.width / 2 + 'px',
                    left: 0
                });
                bigImageDOM.css({
                    top: '-' + config.width + 'px',
                    left: 0
                });
                // 右上
            } else if (
                leftDistance >= 3 * config.width / 4 &&
                topDistance <= config.width / 4
            ) {
                magnifier.css({
                    top: 0,
                    left: config.width / 2 + 'px'
                });
                bigImageDOM.css({
                    top: 0,
                    left: '-' + config.width + 'px'
                });
                // 右下
            } else if (
                leftDistance >= 3 * config.width / 4 &&
                topDistance >= 3 * config.width / 4
            ) {
                magnifier.css({
                    top: config.width / 2 + 'px',
                    left: config.width / 2 + 'px'
                });
                bigImageDOM.css({
                    top: '-' + config.width + 'px',
                    left: '-' + config.width + 'px'
                });
            }
            magnifier.show();
            big.show();
        };

        // 主逻辑
        var mainLogic = function() {
            // 没有触碰到边距
            if (notTouchBorder(leftDistance, topDistance)) {
                magnifier.css({
                    left: leftDistance - config.width / 4 + 'px',
                    top: topDistance - config.width / 4 + 'px'
                });
                bigImageDOM.css({
                    left: -2 * (leftDistance - config.width / 4) + 'px',
                    top: -2 * (topDistance - config.width / 4) + 'px'
                });
            } else {
                // 有一边触碰到了边缘

                // 如果竖直方向上碰到了边缘
                if (
                    leftDistance - config.width / 4 >= 0 &&
                    leftDistance - 3 * config.width / 4 <= 0
                ) {
                    magnifier.css({
                        left: leftDistance - config.width / 4 + 'px'
                    });
                    bigImageDOM.css({
                        left: -2 * (leftDistance - config.width / 4) + 'px'
                    });
                } else if (leftDistance < config.width / 4) {
                    magnifier.css({
                        left: '0px'
                    });
                    bigImageDOM.css({
                        left: '0px'
                    });
                } else if (leftDistance > 3 * config.width / 4) {
                    magnifier.css({
                        left: config.width / 2 + 'px'
                    });
                    bigImageDOM.css({
                        left: '-' + config.width + 'px'
                    });
                }
                // 如果水平方向上碰到了边缘
                if (
                    topDistance - config.width / 4 >= 0 &&
                    topDistance - 3 * config.width / 4 <= 0
                ) {
                    magnifier.css({
                        top: topDistance - config.width / 4 + 'px'
                    });
                    bigImageDOM.css({
                        top: -2 * (topDistance - config.width / 4) + 'px'
                    });
                } else if (topDistance < config.width / 4) {
                    magnifier.css({
                        top: '0px'
                    });
                    bigImageDOM.css({
                        top: '0px'
                    });
                } else if (topDistance > 3 * config.width / 4) {
                    magnifier.css({
                        top: config.width / 2 + 'px'
                    });
                    bigImageDOM.css({
                        top: '-' + config.width + 'px'
                    });
                }
            }
        };

        // 根据配置初始化图片及容器样式
        var setStyle = function(dom) {
            dom.css({
                width: config.width + 'px',
                height: config.width + 'px'
            });
            dom.find('.small,.big,.small img').css({
                width: config.width + 'px',
                height: config.width + 'px'
            });
            dom.find('.big img').css({
                width: 2 * config.width + 'px',
                height: 2 * config.width + 'px'
            });
            dom.find('.magnifier').css({
                width: config.width / 2 + 'px',
                height: config.width / 2 + 'px',
                opacity: config.opacity,
                background: config.background
            });

            // 因为 <ES6 语法不支持对象属性变量，只能写判断了
            if (config.position === 'left') {
                dom.find('.big').css({
                    left: '-' + (config.width + config.distance) + 'px'
                });
            } else if (config.position === 'right') {
                dom.find('.big').css({
                    right: '-' + (config.width + config.distance) + 'px'
                });
            } else if (config.position === 'top') {
                dom.find('.big').css({
                    top: '-' + (config.width + config.distance) + 'px'
                });
            } else if (config.position === 'bottom') {
                dom.find('.big').css({
                    bottom: '-' + (config.width + config.distance) + 'px'
                });
            }
        };

        // 重置变量
        var resetVar = function() {
            magnifier = null;
            bigImageDOM = null;
            leftDistance = undefined;
            topDistance = undefined;
        };

        // 配置赋值
        config = $.extend({}, config, options);
        el.each(function() {
            var $this = $(this);
            resetVar();
            prepareDOM($this);
            bindListener($this);
            setStyle($this);
        });
    };

    $.fn.hiZoom = function(options) {
        start($(this), options);
    };
})(jQuery);
