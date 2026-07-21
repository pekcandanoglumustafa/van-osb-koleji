(function(){
  var hdr = document.getElementById('hdr');
  if(hdr){
    var onScroll = function(){ hdr.classList.toggle('scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  }
  var mm = document.getElementById('mm');
  var burger = document.getElementById('burger');
  var mmClose = document.getElementById('mmClose');
  if(burger && mm){ burger.onclick = function(){ mm.classList.add('open'); document.body.style.overflow='hidden'; }; }
  if(mmClose && mm){ mmClose.onclick = function(){ mm.classList.remove('open'); document.body.style.overflow=''; }; }
  if(mm){
    mm.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ mm.classList.remove('open'); document.body.style.overflow=''; }); });
    // mobile accordion groups
    mm.querySelectorAll('.mm-group .mm-top').forEach(function(btn){
      btn.addEventListener('click', function(){
        var g = btn.parentElement;
        var wasOpen = g.classList.contains('open');
        mm.querySelectorAll('.mm-group').forEach(function(x){ x.classList.remove('open'); });
        if(!wasOpen){ g.classList.add('open'); }
      });
    });
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {threshold:.1, rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.reveal').forEach(function(el,i){ el.style.transitionDelay=(i%4*60)+'ms'; io.observe(el); });
})();
