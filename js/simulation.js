function connect() {
  var edge_dist = 18;
  for (venue1 in venues) {
    for (venue2 in venues) {
      if (venue1 != venue2) {
        if (dist(venues[venue1],venues[venue2]) < edge_dist)
          venues[venue1].edges.push(new Edge(venues[venue2],venues[venue1]));
      }
    }
  }
}
function total_population() {
  var sum_pop = 0;
  for(v in venues) {
    sum_pop += venues[v].population;
  }
  return sum_pop
}

function total_infected() {
  var sum_infected = 0;
  for (v in venues)
    sum_infected += venues[v].infected;
  return sum_infected
}

function update() {
  var sum_incoming_virus = 0;
  for (vi in venues) {
    sum_incoming_virus = 0;
    v = venues[vi]
    for (edgei in v.edges) {
      edge = v.edges[edgei]
      incoming = edge.n1;
      current_node = edge.n2;
      sum_incoming_virus += Math.round(edge.weight*incoming.infected);
    }
    self_virus = Math.round(v.infected * 0.01);
    //console.log("Node " + vi + " gets " + sum_incoming_virus + " from neighbors");
    //console.log("Node " + vi + " has " + v.infected + " infected");
    //console.log("Node " + vi + " has " + v.edges.length + " edges");
    v.new_infected = Math.min(v.infected + sum_incoming_virus + self_virus, v.population)
  }

  for (v in venues) {
    venues[v].infected = venues[v].new_infected;
    //venues[v].population = venues[v].new_population;
  }
}
function randomRange(l,h){
    var range = (h-l);
    var random = Math.floor(Math.random()*range);
    if (random === 0){random+=1;}
    return l+random;
}
function init() {
  connect();
  start_i = randomRange(0,venues.length);
  console.log(venues[start_i]);
  console.log(start_i);
  venues[start_i].infected = Math.round(venues[start_i].population*0.1)
}

function simulate() { //venues is a list of JSON objects
  init();
  console.log("Connected");
  var total_pop = total_population();
  var total_inf= total_infected();
  console.log("Infected: " +  total_inf + ", Total population: " + total_pop);
  while(total_inf < total_pop) {
    update();
    new_total_inf = total_infected();
    console.log("Infected: " +  total_inf + ", Total population: " + total_pop);
    if(total_inf == new_total_inf)
      break;
    total_inf = new_total_inf;
  }
}
