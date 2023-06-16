function yesnoCheck() {
    if (document.getElementById('yesCheck').checked) {
      const l1 = ["Dissolved Oxygen","Bio Chemical Oxygen Demand","Total Coliform","pH"]
      var y = "";
      for(i = 0; i < l1.length; i++){
        y =y + "<option value='"+ l1[i] +"'>"+l1[i]+"</option>"+"<br>";
      };
      document.getElementById("ifYes").innerHTML = y;
    }
    else if (document.getElementById('yesCheck2').checked) {
      const l1 = ["Dissolved Oxygen","Bio Chemical Oxygen Demand","Total Coliform","pH"]
      var y = "";
      for(i = 0; i < l1.length; i++){
        y =y + "<option value='"+ l1[i] +"'>"+l1[i]+"</option>"+"<br>";
      };
      document.getElementById("ifYes").innerHTML = y;
    }
    else if (document.getElementById('yesCheck3').checked) {
      const l1 = ["Dissolved Oxygen","Bio Chemical Oxygen Demand","Total Coliform","pH"]
      var y = "";
      for(i = 0; i < l1.length; i++){
        y =y + "<option value='"+ l1[i] +"'>"+l1[i]+"</option>"+"<br>";
      };
      document.getElementById("ifYes").innerHTML = y;
    }
    else if(document.getElementById('noCheck').checked){
      const l2=['Temperature(°C)', 'Potassium(mg/l)', 'BOD(mg/l)', 'TSS(mg/l)', 'Floride(mg/l)', 
      'Color(µS/cm)', 'BTX(µg/ml)', 'Turbidity(NTU)', 'TOC(mg/l )', 'Chloride(mg/l)', 'Water Level(cm.)', 
      'Nitrate(mg/l)', 'TOC(mg/l)', 'Color(Pt.Scale,Hz units)', 'COD(mg/l)', 'Conductivity(µS/cm)', 'DO(mg/l)', 
      'pH', 'Ammonia(mg/l)']
      var y = "";
      for(i = 0; i < l2.length; i++ ){
        y =y + "<option value='"+l2[i]+"'>"+l2[i]+"</option>"+"<br>";
      };
      document.getElementById("ifYes").innerHTML = y;
    }
  }