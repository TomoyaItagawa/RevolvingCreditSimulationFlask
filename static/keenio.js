function createKeenWebAutoCollector(){window.keenWebAutoCollector=window.KeenWebAutoCollector.create({projectId:{{config.KEEN_PROJECT_ID}},writeKey:{{config.KEEN_WRITE_KEY}},onloadCallbacks:window.keenWebAutoCollector.onloadCallbacks}),window.keenWebAutoCollector.loaded()}function initKeenWebAutoCollector(){window.keenWebAutoCollector.domReady()?window.createKeenWebAutoCollector():document.addEventListener("readystatechange",function(){window.keenWebAutoCollector.domReady()&&window.createKeenWebAutoCollector()})}window.keenWebAutoCollector={onloadCallbacks:[],onload:function(a){this.onloadCallbacks.push(a)},domReady:function(){return["ready","complete"].indexOf(document.readyState)>-1}};
