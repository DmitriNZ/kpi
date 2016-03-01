
import moment from 'moment';
import alertify from 'alertifyjs';
import $ from 'jquery';
import translations from './translations.json';

export var assign = require('react/lib/Object.assign');

export function notify(msg, atype='success') {
  alertify.notify(msg, atype);
}

export function formatTime(timeStr) {
  var _m = moment(timeStr);
  return _m.fromNow();
}

export var anonUsername = 'AnonymousUser';
export function getAnonymousUserPermission(permissions) {
  return permissions.filter(function(perm){
    return perm.user__username === anonUsername;
  })[0];
}

export function surveyToValidJson(survey) {
  return JSON.stringify(survey.toFlatJSON());
}

export function customPromptAsync(msg) {
  return new Promise(function(resolve, reject){
    window.setTimeout(function(){
      var val = window.prompt(msg);
      if (val === null) {
        reject(new Error('empty value'));
      } else {
        resolve(val);
      }
    }, 0);
  });
}

export function customConfirmAsync(msg) {
  var dfd = new $.Deferred();
  window.setTimeout(function(){
    var tf = window.confirm(msg);
    dfd[ tf ? 'resolve' : 'reject' ](tf);
  }, 0);
  return dfd.promise();
}

export function customConfirm(msg) {
  /*eslint no-alert: 0*/
  return window.confirm(msg);
}
export function customPrompt(msg) {
  /*eslint no-alert: 0*/
  return window.prompt(msg);
}

export function redirectTo(href) {
  window.location.href = href;
}

export function parsePermissions(owner, permissions) {
  var users = [];
  var perms = {};
  if (!permissions) {
    return [];
  }
  permissions.map((perm) => {
    perm.user__username = perm.user.match(/\/users\/(.*)\//)[1];
    return perm;
  }).filter((perm)=> {
    return ( perm.user__username !== owner && perm.user__username !== anonUsername);
  }).forEach((perm)=> {
    if(users.indexOf(perm.user__username) === -1) {
      users.push(perm.user__username);
      perms[perm.user__username] = [];
    }
    perms[perm.user__username].push(perm);
  });
  return users.map((username)=>{
    return {
      username: username,
      can: perms[username].reduce((cans, perm)=> {
        var permCode = perm.permission.split('_')[0];
        cans[permCode] = perm;
        return cans;
      }, {})
    };
  });
}


export var log = (function(){
  var _log = function(...args) {
    console.log.apply(console, args);
    return args[0];
  };
  _log.profileSeconds = function(n=1) {
    console.profile();
    window.setTimeout(function(){
      console.profileEnd();
    }, n * 1000);
  };
  return _log;
})();
window.log = log;


var __strings = [];


var cookie = require('cookie-cutter');
const DEFAULT_LANGUAGE = 'en';

export function currentLang() {
  var languageCode = cookie.get('django_language');
  if (languageCode === 'debug') {
    return languageCode;
  } else if (!languageCode || !translations[languageCode]) {
    return DEFAULT_LANGUAGE;
  }
  return languageCode;
}

var cookieDomainMeta = document.head.querySelector('meta[name=cookie-domain]');
if (cookieDomainMeta && !cookie.get('domain')) {
  log('setting cookie domain to ', cookieDomainMeta.content);
  cookie.set('domain', cookieDomainMeta.content);
}

export function setLang(langCode) {
  if (langCode === 'debug' || translations[langCode]) {
    cookie.set('django_language', langCode);
  } else {
    throw new Error(`language '${langCode}' not found in translations.json`);
  }
}

export function languagePrompt () {
  var langPromptStr = [
    'language code?',
    `current:${currentLang()}`,
    `available:${Object.keys(translations).join(',')}`,
  ].join(' ');

  return new Promise(function(success, fail){
    customPromptAsync(langPromptStr).then(function(lang){
      setLang(lang);
      success(lang);
    }).catch(function(){
      fail();
    });
  });
};


export function t_(str) {
  // returns the translated string with some extra context
  var _cl = currentLang();
  if (_cl === 'debug') {
    var rx = Math.floor(Math.random() * 2);
    var wEiRdCaPs = Array.prototype.slice.call(str).map(function(x, n){
      return x[n % 2 === rx ? 'toUpperCase' : 'toLowerCase']();
    }).join('');
    return ['«' + wEiRdCaPs + '»', {lang: 'debug', debug: true}]
  }
  if (translations[_cl][str]) {
    return [translations[_cl][str], {lang: _cl}];
  }
  if (__strings.indexOf(str) === -1) {
    __strings.push(str);
  }
  return [str, {raw: true}];
};

export function t(str) {
  return t_(str)[0];
}

log.t = function () {
  let _t = {};
  __strings.forEach(function(str){ _t[str] = str; })
  console.log(JSON.stringify(_t, null, 4));
};

// unique id for forms with inputs and labels
let lastId = 0;
export var newId = function(prefix='id') {
    lastId++;
    return `${prefix}${lastId}`;
};
