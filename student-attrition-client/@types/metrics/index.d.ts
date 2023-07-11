export interface IMetricData {
  marital_status: null | string,
  application_mode: null | string,
  application_order: null | number,
  course: null | string,
  attendance_type: null | string,
  previous_qualification: null | string,
  nationality: null | string,
  mothers_qualification: null | string,
  fathers_qualification: null | string,
  mothers_occupation: null | string,
  fathers_occupation: null | string,
  displaced: null | string,
  educational_special_needs: null | string,
  debtor: null | string,
  tuition_fees_up_to_date: null | string,
  gender: null | string,
  scholarship_holder: null | string,
  age_at_enrolment: null | number,
  international: null | string,
  curricular_units_1st_semester_credited: null | number,
  curricular_units_1st_semester_enrolled: null | number,
  curricular_units_1st_semester_evaluations: null | number,
  curricular_units_1st_semester_approved: null | number,
  curricular_units_1st_semester_grade: null | number,
  curricular_units_1st_semester_without_evaluations: null | number,
  curricular_units_2nd_semester_credited: null | number,
  curricular_units_2nd_semester_enrolled: null | number,
  curricular_units_2nd_semester_evaluations: null | number,
  curricular_units_2nd_semester_approved: null | number,
  curricular_units_2nd_semester_grade: null | number,
  curricular_units_2nd_semester_without_evaluations: null | number,
  unemployment_rate: null | number,
  inflation_rate: null | number,
  gdp: null | number
}

export interface IMetricResultsFeatureDict {
  academic: number;
  finance: number;
  supportNetwork: number;
}

export interface IMetricResults {
  featureDict: IMetricResultsFeatureDict
  featureMain: string,
  featureStrength: number,
  label: string,
  score: number,
  optimumCategory: string,
  optimumCategoryValue: number
}


export interface IMetricState {
  data: IMetricData
  analysingPerformance: boolean
  resultsExist: boolean,
  results: IMetricResults
}


export interface IMetricOptions {
  name: null | string;
  marital_status: null | string[];
  application_mode: null | string[];
  course: null | string[];
  attendance_type: null | string[];
  previous_qualification: null | string[];
  nationality: null | string[];
  parental_qualification: null | string[];
  parental_occupation: null | string[];
  binary: null | string[];
  gender: null | string[];
}