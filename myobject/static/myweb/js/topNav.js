/*购物车--------------------------------------------*/ 

//选择框操作
function allSelect(){
  var aee = false;
  var see = false;
  // 全选
  $('.JSelectAll .mz-checkbox').click(function(){
    if(aee==false){
      $(this).addClass('checked');
      $('.cart-col-select .mz-checkbox').addClass('checked');
      aee = true;
    }else if(aee==true){
      $(this).removeClass('checked');
      $('.cart-col-select .mz-checkbox').removeClass('checked');
      aee = false;
    }
    loadTotal();
  })

  //单选
  $('.cart-col-select .mz-checkbox').click(function(){
    $(this).toggleClass("checked");
    loadTotal();
  })
}

//计算商品数量和总金额
function loadTotal(){
    var ids = [];
    //alert('ok');
    //获取所有选择的商品
    var list = $("table.cart-merchant-body div.mz-checkbox").filter(".checked");
    $("#totalCount").html(list.length);
    var total = 0.0;
    for(var i=0;i<list.length;i++){
       total += parseFloat($(list[i]).attr('price'));
       ids.push($(list[i]).attr('gid'));
    }
    //alert(total);
    $("#totalPrice").html(total);
    return ids;
}

// 数量增加减少
function cartAddMin(){
      var pList = $('.cart-product');
      //页面底部显示初始值
      //初始商品总数量
      $('#totalCount').html(pList.length); 
      var fsnC = Number( $('#totalCount').text());

      //初始商品总和
      var i = 0;
      var fsPrice = 0;

      while(i<pList.length){
        // var v = pList.eq(i).index();
        var sPrice=Number($('.cart-product').eq(i).find('.cart-product-price.total').text());
        var fsPrice = Number(fsPrice)+Number(sPrice);
        i++;
        $('#totalPrice').html(fsPrice+'.00');
      }

      
      // 减少
      $('.mz-adder-subtract').click(function(){
           //检测操作的是哪个商品
           var fzhi=$(this).parents('.cart-product').attr('id');
           var reg=/^pro\d$/;
           var prod=reg.exec(fzhi);

           //商品展示个数、减号、超过数量的文本
           var $mText = $(this).parents('#'+prod).find('.cart-product-number-max');
           var $nSub = $(this).parents('#'+prod).find('.mz-adder-subtract');
           var $nInput = $(this).parents('#'+prod).find('.mz-adder-input');
           var n=$nInput.val();
           var num=parseInt(n)-1;

           

           //获取当前商品的单价和小计
           var $nPrice = $(this).parents('#'+prod).find('.cart-col-price .cart-product-price');
           var npText = parseInt($nPrice.text());
           var $sumPrice = $(this).parents('#'+prod).find('.cart-col-total  .cart-product-price');
           var spText = parseInt($sumPrice.text());

           //单个商品的小计
           spText= spText - npText;
           $sumPrice.html(spText+'.00');
            
           
           //商品减少操作
           if(num<=1){ 
              $nSub.addClass('disabled');
              $nInput.val(1);
           }else if(num>1){
              $nInput.val(num);
           }
           if(num<5){
              $mText.removeClass('show');
           }

           //页面底部显示一共多少商品和选择的商品个数
           var fsNum = Number( $('#totalCount').text());
           var newNum = fsNum-1;
           $('#totalCount').html(newNum);

           //页面底部总和
           var fPrice=$('#totalPrice').text();
           var regs=/\d+/;
           var sfPrice= Number(regs.exec(fPrice));

           //算出新的总价格
           var nsfPrice=spText+sfPrice;
           $('#totalPrice').html(nsfPrice+'.00');

      })
      //增加
      $('.mz-adder-add').click(function(){
           //检测操作的是哪个商品
           var fzhi=$(this).parents('.cart-product').attr('id');
           var reg=/^pro\d$/;
           var prod=reg.exec(fzhi);

           //商品展示个数、加号、超过数量的文本
           var $nAdd = $(this).parents('#'+prod).find('.mz-adder-add');
           var $nSub = $(this).parents('#'+prod).find('.mz-adder-subtract');
           var $nInput = $(this).parents('#'+prod).find('.mz-adder-input');
           var n=$nInput.val();
           var $mText = $(this).parents('#'+prod).find('.cart-product-number-max');
           var num=parseInt(n)+1;

           //获取当前商品的单价和小计
           var $nPrice = $(this).parents('#'+prod).find('.cart-col-price .cart-product-price');
           var npText = parseInt($nPrice.text());
           var $sumPrice = $(this).parents('#'+prod).find('.cart-col-total  .cart-product-price');
           var spText = parseInt($sumPrice.text());


           
           //商品增加操作
           if(num>1){ 
                $nSub.removeClass('disabled');
                $nInput.val(num);

           }
           if(num==5){
                $nAdd.addClass('disabled');
                $mText.addClass('show');
                $mText.text("限购5件");
                $nInput.val(num);
           } 
           if(num>5){ 
                $nAdd.addClass('disabled');
                $mText.addClass('show');
                $mText.text("限购5件");
                $nInput.val(5);
               return false;
           }
           //单个商品的小计
           spText= spText + npText;
           $sumPrice.html(spText+'.00');
           // console.log(num);

           //页面底部显示一共多少商品和选择的商品个数
           var fsNum = Number( $('#totalCount').text());
           var newNum = fsNum+1;
           $('#totalCount').html(newNum);


           //页面底部总和
           var fPrice=$('#totalPrice').text();
           var regs=/\d+/;
           var sfPrice= Number(regs.exec(fPrice));


           //算出新的总价格
           var nsfPrice=spText+sfPrice;
           $('#totalPrice').html(nsfPrice+'.00');
           console.log(sfPrice)
      })

      //叉号删除商品

      $('.cart-product-remove').click(function(){
            $(this).parents('.cart-product').remove();
      })

    
}// 数量增加减少E 

/*---------------------------------------------------*/ 
