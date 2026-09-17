export const doctors = [
  {
    id: 'speed',
    name: 'DR. SPEED',
    subtitle: '快刀醫師',
    bonusText: '備料正確時 Focus +8',
    portrait: 'assets/concept/doctor_concepts.svg',
    prepFocusBonus: 8,
    heatTolerance: 0,
    timeSlow: 1
  },
  {
    id: 'heat',
    name: 'DR. HEAT',
    subtitle: '火候醫師',
    bonusText: '最佳火候區 +12%',
    portrait: 'assets/concept/doctor_concepts.svg',
    prepFocusBonus: 4,
    heatTolerance: 12,
    timeSlow: 1
  },
  {
    id: 'strategy',
    name: 'DR. STRATEGY',
    subtitle: '處方醫師',
    bonusText: 'Craving 上升速度 -18%',
    portrait: 'assets/concept/doctor_concepts.svg',
    prepFocusBonus: 4,
    heatTolerance: 4,
    timeSlow: 0.82
  }
];

export const ingredients = [
  { id:'tofu', label:'豆腐', icon:'⬜' },
  { id:'pork', label:'絞肉', icon:'🥩' },
  { id:'douban', label:'豆瓣醬', icon:'🌶️' },
  { id:'garlic', label:'蒜末', icon:'🧄' },
  { id:'pepper', label:'花椒', icon:'🫙' },
  { id:'scallion', label:'青蔥', icon:'🌿' },
  { id:'rice', label:'白飯', icon:'🍚' },
  { id:'chili', label:'辣椒', icon:'🌶️' }
];

export const patients = [
  {
    id:'office',
    name:'焦慮上班族',
    portrait:'assets/concept/patient_npcs.svg',
    line:'「會議還有二十分鐘……麻婆豆腐可以快一點嗎？」',
    order:{ spice:'中辣', rice:'飯多', modifier:'快速出餐', required:['tofu','pork','douban','garlic','pepper','rice'] }
  },
  {
    id:'student',
    name:'熬夜學生',
    portrait:'assets/concept/patient_npcs.svg',
    line:'「小辣，豆腐多一點，不要蔥……我等等還要讀書。」',
    order:{ spice:'小辣', rice:'正常', modifier:'不要蔥', required:['tofu','pork','douban','garlic','pepper'] }
  },
  {
    id:'driver',
    name:'長班司機',
    portrait:'assets/concept/patient_npcs.svg',
    line:'「今天開了一整天。我要大辣、飯多、蔥多。」',
    order:{ spice:'大辣', rice:'飯多', modifier:'蔥多', required:['tofu','pork','douban','garlic','pepper','chili','scallion','rice'] }
  },
  {
    id:'auntie',
    name:'熱情阿姨',
    portrait:'assets/concept/patient_npcs.svg',
    line:'「醫師你們也要記得吃飯喔。我的豆腐多一點！」',
    order:{ spice:'中辣', rice:'飯多', modifier:'豆腐多', required:['tofu','pork','douban','garlic','pepper','scallion','rice'] }
  },
  {
    id:'quiet',
    name:'安靜青年',
    portrait:'assets/concept/patient_npcs.svg',
    line:'「中辣就好……不要蔥，謝謝。」',
    order:{ spice:'中辣', rice:'正常', modifier:'不要蔥', required:['tofu','pork','douban','garlic','pepper'] }
  },
  {
    id:'repeat',
    name:'熟客',
    portrait:'assets/concept/patient_npcs.svg',
    line:'「一樣的，一樣的。今天……可以再辣一點。」',
    order:{ spice:'特辣', rice:'飯多', modifier:'熟客配方', required:['tofu','pork','douban','garlic','pepper','chili','rice'] }
  }
];

export const cookSteps = ['爆香','炒肉','下豆腐','勾芡收汁'];
