//  declaring the variable for making a copy
// for  co-ordinates drawn on the map
var varival;

// create an OSM layer of Map
var osm= new ol.layer.Tile({
    title: 'OSM',
    source: new ol.source.OSM()
});

// create a vector layer for the Map
//  add different different properties for that vector layer
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
// add the above created OSM and Vector layer in a Map 
var map = new ol.Map({
    layers: [osm, vector],
    target: 'map',
    view: new ol.View({
        center: ol.proj.fromLonLat([75.9, 22.4]),
        zoom: 4
    })
});

// declaring a variable for starting the logic 
// check whether the option-form is selected or not
var optionsForm = document.getElementById('options-form');

// Draw method for providing theother types for printing
var Draw = {
    // decalre the draw init function
    init: function() {
        // check the interection type
        //  either it a point 
        map.addInteraction(this.Point);
        this.Point.setActive(false);
        
        // check the interection type
        //  either it a polygon 
        map.addInteraction(this.Polygon);
        this.Polygon.setActive(false);
    },

    // define the point interection functionality
    Point: new ol.interaction.Draw({
        source: vector.getSource(),
        type: /** @type {ol.geom.GeometryType} */ ('Point')
    }),
    
    // define the polygon interection functionality
    Polygon: new ol.interaction.Draw({
        source: vector.getSource(),
        type: /** @type {ol.geom.GeometryType} */ ('Polygon')
    }),

    // create getActive function for the draw part
    getActive: function() {
        
        return this.activeType ? this[this.activeType].getActive() : false;
    },

    // create setActive function for the draw part
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
// call that function 
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
            
            var features = vector.getSource().getFeatures();
            features.forEach(function(feature) {
                console.log(feature.getGeometry().getCoordinates());
                
            });
        } else if (value == 'draw') {
            Draw.setActive(true);
        }
    }
};

/* set the coordinate value into the coordinate
part of  the html template of our site */
document.getElementById("idhai").onclick = function(e){
    var pointval = document.getElementById("point").innerHTML;
    pointval = "";
    console.log("worked");
    var features = vector.getSource().getFeatures();
    features.forEach(function(feature) {
        varival = feature.getGeometry().getCoordinates();
        if(varival.length != 1){
            pointval += feature.getGeometry().getCoordinates() + "\n";
        }
        else{
            for(var j=0; j<varival[0].length - 1; j++){
                pointval += varival[0][j] + ",  ";
            }
        }
    });
    document.getElementById("point").innerHTML = pointval;
};

// set the status of Draw object
Draw.setActive(true);

// The snap interaction must be added after the Modify and Draw interactions
// in order for its map browser event handlers to be fired first. Its handlers
// are responsible of doing the snapping.
var snap = new ol.interaction.Snap({
    source: vector.getSource()
});
map.addInteraction(snap);