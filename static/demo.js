//  declaring the variable for making a copy
// for  co-ordinates drawn on the map
var varival;

// create an OSM layer of Map
var osm= new ol.layer.Tile({
    title: 'OSM',
    source: new ol.source.OSM()
});

// create a vector layer for the Map
var vector = new ol.layer.Vector({
    source: new ol.source.Vector(),
    style: new ol.style.Style({
        fill: new ol.style.Fill({
            color: 'rgba(255, 255, 255, 0.2)'
        }),
        stroke: new ol.style.Stroke({
            color: '#ffcc33',
            width: 2
        }),
        image: new ol.style.Circle({
            radius: 7,
            fill: new ol.style.Fill({
                color: '#ffcc33'
            })
        })
    })
});

// create a Map layer for Map 
// and pointing it to initial coordinates i.e. "75.9, 22.4"
var map = new ol.Map({
    layers: [osm, vector],
    target: 'map',
    view: new ol.View({
        center: ol.proj.fromLonLat([75.9, 22.4]),
        zoom: 4
    })
});

// // creating a function for modifying the type of drawn object on the map
// var Modify = {
//     // init function of the method
//     init: function() {
//         this.select = new ol.interaction.Select();
//         map.addInteraction(this.select);
//         this.modify = new ol.interaction.Modify({
//             features: this.select.getFeatures()
//         });
//         map.addInteraction(this.modify);
//         this.setEvents();
//     },

//     // setEent function of the created method
//     setEvents: function() {
//         var selectedFeatures = this.select.getFeatures();
//         this.select.on('change:active', function() {
//             selectedFeatures.forEach(selectedFeatures.remove, selectedFeatures);
//         });
        
//     },

//     // setActive function of the created method
//     setActive: function(active) {
//         this.select.setActive(active);
//         this.modify.setActive(active);
        
//     }
// };
// Modify.init();

var optionsForm = document.getElementById('options-form');

var Draw = {
    init: function() {
        map.addInteraction(this.Point);
        this.Point.setActive(false);
        // map.addInteraction(this.LineString);
        // this.LineString.setActive(false);
        map.addInteraction(this.Polygon);
        this.Polygon.setActive(false);
    },
    Point: new ol.interaction.Draw({
        source: vector.getSource(),
        type: /** @type {ol.geom.GeometryType} */ ('Point')
    }),
    // LineString: new ol.interaction.Draw({
    //     source: vector.getSource(),
    //     type: /** @type {ol.geom.GeometryType} */ ('LineString')
    // }),
    Polygon: new ol.interaction.Draw({
        source: vector.getSource(),
        type: /** @type {ol.geom.GeometryType} */ ('Polygon')
    }),
    getActive: function() {
        
        return this.activeType ? this[this.activeType].getActive() : false;
    },
    setActive: function(active) {
        var type = optionsForm.elements['draw-type'].value;
        if (active) {
            this.activeType && this[this.activeType].setActive(false);
            this[type].setActive(true);
            this.activeType = type;
        } 
        else {
            this.activeType && this[this.activeType].setActive(false);
            this.activeType = null;
        }   
    }
};
Draw.init();

/** Let user change the geometry type. @param {Event} e Change event. */
optionsForm.onchange = function(e) {
    console.log("hello1");
    var type = e.target.getAttribute('name');
    var value = e.target.value;
    if (type == 'draw-type') {
        Draw.getActive() && Draw.setActive(true);
        console.log("hello2");
    } 
    else if (type == 'interaction') {
        console.log("hello3");
        if (value == 'modify') {
            console.log("hello4");
            Draw.setActive(false);
            // Modify.setActive(true);
            var features = vector.getSource().getFeatures();
            features.forEach(function(feature) {
                console.log(feature.getGeometry().getCoordinates());
                
            });
        } else if (value == 'draw') {
            Draw.setActive(true);
            // Modify.setActive(false);
        }
    }
};

document.getElementById("idhai").onclick = function(e){
    var pointval = document.getElementById("point").innerHTML;
    pointval = "";
    console.log("worked");
    var features = vector.getSource().getFeatures();
    features.forEach(function(feature) {
        //document.getElementById("point").innerHTML = feature.getGeometry().getCoordinates();
        varival = feature.getGeometry().getCoordinates();
        if(varival.length != 1){
            pointval += feature.getGeometry().getCoordinates() + "\n";
        }
        else{
            for(var j=0; j<varival[0].length - 1; j++){
                pointval += varival[0][j] + "\n";
            }
        }
    });
    // console.log(varival.length);
    // console.log(typeof varival[0]);
    // console.log(varival[0]);
    // console.log(pointval);
    // console.log(typeof pointval[0]);
    document.getElementById("point").innerHTML = pointval;
};

Draw.setActive(true);
// Modify.setActive(false);

// The snap interaction must be added after the Modify and Draw interactions
// in order for its map browser event handlers to be fired first. Its handlers
// are responsible of doing the snapping.
var snap = new ol.interaction.Snap({
    source: vector.getSource()
});
map.addInteraction(snap);