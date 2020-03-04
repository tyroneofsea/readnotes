<!--WAP底部悬浮-->
<style>
@media screen and (max-device-width:800px){ /**WAP**/
.bottom_fixed{ position:fixed; bottom:0px; width:100%; z-index:9999;right:0;left:0}
.bottom_fixed div{ width:60px; height:20px;background-color:transparent; text-align:center; line-height:20px; right:0; top:-20px; position:absolute; cursor:pointer;}
.bottom_fixed div:hover{ background:#F66; color:#FFF}
.bottom_fixed a{text-decoration:none; color:black}
.bottom_fixed a img{ height:95px; width:100%;}
}
@media screen and (min-width:800px){ /**PC**/
.bottom_fixed{ display:none; position:fixed; bottom:0px; left:50%; margin-left:-475px; z-index:9999;}
.bottom_fixed div{ width::50px; height:24px; text-align:center; line-height:24px;background-color:transparent; right:0; top:-24px; position:absolute; cursor:pointer}
.bottom_fixed div:hover{ background:#F66; color:#FFF}
.bottom_fixed a{text-decoration:none; color:black}
.bottom_fixed a img{ height:75px; width:950px;}
}
</style>
<div class="bottom_fixed">
<a href="链接地址" rel="nofollow" target="_blank"><img id="sjdfjkjimg" src="图片链接地址"><div>不再显示</div></a>
</div>

<script>
var imgs =["1.jpg", "2.jpg", "3.jpg"];    //（设定想要显示的图片）
var x = 0;       
function time1(){

x++;   
x=x%3;         //         超过2则取余数，保证循环在0、1、2之间
var  imgurl="图片链接地址"+imgs[x];
document.getElementById("sjdfjkjimg").src  =imgurl;
console.log(imgurl)
}
setInterval('time1()',5000);
</script>
