
<style>

  /* Leaflet.label.css */
  .leaflet-label {
    background: rgb(235, 235, 235);
    background: rgba(235, 235, 235, 0.81);
    background-clip: padding-box;
    border-color: #777;
    border-color: rgba(0,0,0,0.25);
    border-radius: 4px;
    border-style: solid;
    border-width: 4px;
    color: #111;
    display: block;
    font: 12px/20px "Helvetica Neue", Arial, Helvetica, sans-serif;
    font-weight: bold;
    padding: 1px 6px;
    position: absolute;
    -webkit-user-select: none;
       -moz-user-select: none;
        -ms-user-select: none;
            user-select: none;
    pointer-events: none;
    white-space: nowrap;
    z-index: 6;
  }

  .leaflet-label.leaflet-clickable {
    cursor: pointer;
    pointer-events: auto;
  }

  .leaflet-label:before,
  .leaflet-label:after {
    border-top: 6px solid transparent;
    border-bottom: 6px solid transparent;
    content: none;
    position: absolute;
    top: 5px;
  }

  .leaflet-label:before {
    border-right: 6px solid black;
    border-right-color: inherit;
    left: -10px;
  }

  .leaflet-label:after {
    border-left: 6px solid black;
    border-left-color: inherit;
    right: -10px;
  }

  .leaflet-label-right:before,
  .leaflet-label-left:after {
    content: "";
  }

  /* Leaflet.label.css */
      #mymap {
        width: 800px;
        height: 500px;
      }

      .info {
        padding: 6px 8px;
        font: 14px/16px Arial, Helvetica, sans-serif;
        background: white;
        background: rgba(255,255,255,0.8);
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
        border-radius: 5px;
      }
      .info h4 {
        margin: 0 0 5px;
        color: #777;
      }

      .legend {
        text-align: left;
        line-height: 18px;
        color: #555;
      }
      .legend i {
        width: 18px;
        height: 18px;
        float: left;
        margin-right: 8px;
        opacity: 0.7;
      }
</style>

<div class="row">
        <!-- Left col -->
        <section class="col-lg-7 connectedSortable">
          <!-- Custom tabs (Charts with tabs)-->
          <div class="nav-tabs-custom">
            <!-- Tabs within a box -->
            <ul class="nav nav-tabs pull-right">
              <li class="active"><a href="#revenue-chart" data-toggle="tab">नक्सा</a></li>
              <!-- <li><a href="#sales-chart" data-toggle="tab">Donut</a></li> -->
              <li class="pull-left header"><i class="fa fa-inbox"></i> पर्वतको नक्सा</li>
            </ul>
            <div class="tab-content no-padding">
              <!-- Morris chart - Sales -->
              <div class="chart tab-pane active" id="revenue-chart" style="position: relative; height: 700px;"></div>
              <div class="chart tab-pane" id="sales-chart" style="position: relative; height: 700px;"></div>
            </div>
          </div>
          <!-- /.nav-tabs-custom -->
        </section>
      
        <script type="text/javascript">
          var mycss=['leaflet.css'];
          var myjs = 
           ['jquery.min.js','leaflet.js','Label.js', 'BaseMarkerMethods.js','Marker.Label.js','CircleMarker.Label.js','Path.Label.js','Map.Label.js','FeatureGroup.Label.js'];

            function loadjscssfile(filename, filetype){
              if (filetype=="js"){ //if filename is a external JavaScript file
                  /*var fileref=document.createElement('script')
                  fileref.setAttribute("type","text/javascript")
                  fileref.setAttribute("src", filename)*/
                  var element = document.createElement("script");
                  element.src = filename;
                  document.body.appendChild(element);
              }
              else if (filetype=="css"){ //if filename is an external CSS file
                  var fileref=document.createElement("link")
                  fileref.setAttribute("rel", "stylesheet")
                  fileref.setAttribute("type", "text/css")
                  fileref.setAttribute("href", filename)
              }
              if (typeof fileref!="undefined")
                  document.getElementsByTagName("head")[0].appendChild(fileref)
            }




        /*loadjscssfile("myscript.js", "js") //dynamically load and add this .js file
        loadjscssfile("javascript.php", "js") //dynamically load "javascript.php" as a JavaScript file
        loadjscssfile("mystyle.css", "css") ////dynamically load and add this .css file
        */
        </script>
        <div id="mapinfo" class="col-lg-8"></div>
        <script type="text/javascript">
           function showValue(newValue, target)    {
              document.getElementById(target).innerHTML=newValue;    
            }
      </script>

      <div id="map" style="height:600px; width:1200px;align:center;"></div>

</div>

<?php include_once 'more.php'; ?>

<script type="text/javascript">
  function downloadJSAtOnload() {
   var element = document.createElement("script");
   // element.src = "defer.js";
   document.body.appendChild(element);
  }
  if (window.addEventListener)
   window.addEventListener("load", downloadJSAtOnload, false);
  else if (window.attachEvent)
   window.attachEvent("onload", downloadJSAtOnload);
  else window.onload = downloadJSAtOnload;
</script>

<div id="scripts_mymap">
<script type="text/javascript">
for (var i = mycss.length - 1; i >= 0; i--) {
   mycss[i] = "../../src/" + mycss[i];
   console.log(mycss[i]);
   loadjscssfile(mycss[i], "css");
 }


for (var i = 0; i < myjs.length ; i++) {

   myjs[i] = "../../src/" + myjs[i] ;
   console.log(myjs[i]);
   loadjscssfile(myjs[i], "js");
 }
loadjscssfile("../../Lmap2.js", "js");  
</script>
<script type="text/javascript" src="../../Lmap2.js"></script>
 </div>
