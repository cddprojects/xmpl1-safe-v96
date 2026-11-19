(function(){
  var btn=document.querySelector('.menu-btn'),list=document.getElementById('nav-list');
  if(btn&&list){btn.addEventListener('click',function(){
    var o=list.classList.toggle('open');btn.setAttribute('aria-expanded',o);btn.setAttribute('aria-label',o?'Zamknij menu':'Otwórz menu');});}

  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  }else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});}

  var chips=document.querySelectorAll('.chip[data-filter]');
  chips.forEach(function(c){c.addEventListener('click',function(){
    chips.forEach(function(x){x.setAttribute('aria-pressed',x===c);});
    var f=c.dataset.filter;
    document.querySelectorAll('.post[data-cat]').forEach(function(p){
      p.hidden=!(f==='all'||p.dataset.cat===f);});});});

  var s=document.getElementById('glossary-search');
  if(s){s.addEventListener('input',function(){
    var q=s.value.trim().toLowerCase(),n=0;
    document.querySelectorAll('.term').forEach(function(t){
      var m=t.textContent.toLowerCase().indexOf(q)>-1;t.hidden=!m;if(m)n++;});
    document.getElementById('glossary-empty').hidden=n>0;});}

  var chk=document.getElementById('scam-check');
  if(chk){
    var out=document.getElementById('scam-result');
    var update=function(){
      var n=chk.querySelectorAll('input:checked').length,h,p,c='result';
      if(n===0){out.hidden=true;return;}
      if(n===1){c+=' warn';h='Jeden sygnał ostrzegawczy. Zwolnij.';p='Zanim cokolwiek wyślesz, znajdź firmę samodzielnie: KRS albo CEIDG, strona kariery i numer w KRAZ, jeśli pisze agencja.';}
      else{c+=' bad';h=n+' sygnały. Traktuj to jak prawdopodobne oszustwo.';p='Przestań odpisywać. Nie wysyłaj pieniędzy, zdjęcia dowodu, PESEL-u, kodu BLIK ani loginu do banku. Jeśli pieniądze już wyszły, zadzwoń do banku i na Policję. Incydent możesz zgłosić w CERT Polska.';}
      out.className=c;out.hidden=false;out.querySelector('h3').textContent=h;out.querySelector('p').textContent=p;};
    chk.addEventListener('change',update);
  }

  var f=document.getElementById('contact-form');
  if(f){f.addEventListener('submit',function(e){
    e.preventDefault();var ok=true;
    f.querySelectorAll('[required]').forEach(function(i){
      var err=i.parentElement.querySelector('.err'),bad=!i.value.trim()||(i.type==='email'&&!/^\S+@\S+\.\S+$/.test(i.value));
      err.textContent=bad?(i.type==='email'?'Podaj poprawny adres e-mail.':'To pole jest wymagane.'):'';
      i.setAttribute('aria-invalid',bad);if(bad)ok=false;});
    if(ok){
      var v=function(id){var e=document.getElementById(id);return e?e.value.trim():'';};
      var subj='Wiadomość ze strony'+(v('topic')?': '+v('topic'):'');
      var body='Imię: '+v('name')+'\nE-mail: '+v('email')+'\n\n'+v('msg');
      f.hidden=true;var okEl=document.getElementById('form-ok');okEl.hidden=false;okEl.focus();
      window.location.href='mailto:kontakt@nimblyquest.com?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(body);
    }
  });}

  function num(el){return parseFloat(String(el.value).replace(/\s/g,'').replace(',','.'));}
  function pln(n){return n.toLocaleString('pl-PL',{minimumFractionDigits:n%1?2:0,maximumFractionDigits:2});}

  var cf=document.getElementById('calc');
  if(cf){
    var t=document.getElementById('c-target'),r=document.getElementById('c-rate'),o=document.getElementById('c-out');
    var run=function(){var a=num(t),b=num(r);
      if(!(a>0)||!(b>0)){o.hidden=true;return;}
      var h=a/b/4.33;
      var hf=(Math.round(h*10)/10).toLocaleString('pl-PL');
      var note='';
      if(b<31.4){note='<br>Od 1 stycznia 2026 r. minimalna stawka godzinowa przy części umów zlecenia to 31,40 zł brutto. Nie każda umowa jej podlega. Jeśli ogłoszenie jest niżej, dopytaj dlaczego.';}
      o.innerHTML='<b>Około '+hf+' godz. tygodniowo</b><br>żeby dojść do '+pln(a)+' zł miesięcznie przy '+pln(b)+' zł za godzinę, przed podatkiem i kosztami. To szacunek, nie obietnica wynagrodzenia.'+note;o.hidden=false;};
    t.addEventListener('input',run);r.addEventListener('input',run);
  }
})();
