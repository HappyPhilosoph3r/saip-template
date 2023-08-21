import {PerformanceMetricOptions} from "../models/PerformanceMetricOptions";
import logger from "../utils/logger";

export async function createPerformanceMetricOptions(): Promise<boolean>{
  /** Creates an instance of performance metric options in the database, containing all relevant options. */
  try{
    const options = new PerformanceMetricOptions({
      marital_status: ["Single", "Married", "Widower", "Divorced", "Facto union", "Legally separated"],
      application_mode: ["1st phase—general contingent", "Ordinance No. 612/93",
        "1st phase—special contingent (Azores Island)", "Holders of other higher courses", "Ordinance No. 854-B/99",
        "International student (bachelor)", "1st phase—special contingent (Madeira Island)",
        "2nd phase—general contingent", "3rd phase—general contingent",
        "Ordinance No. 533-A/99, item b2) (Different Plan)",  "Ordinance No. 533-A/99, item b3 (Other Institution)",
        "Over 23 years old",  "Transfer",  "Change in course",  "Technological specialization diploma holders",
        "Change in institution/course",  "Short cycle diploma holders",
        "Change in institution/course (International)"],
      course: ["Biofuel Production Technologies",  "Animation and Multimedia Design",
        "Social Service (evening attendance)", "Agronomy", "Communication Design", "Veterinary Nursing",
        "Informatics Engineering", "Equiniculture", "Management",  "Social Service",  "Tourism",  "Nursing",
        "Oral Hygiene",  "Advertising and Marketing Management",  "Journalism and Communication",  "Basic Education",
        "Management (evening attendance)"],
      attendance_type: ["Evening", "Daytime"],
      previous_qualification: ["Secondary education",  "Higher education—bachelor’s degree", "Higher education—degree",
        "Higher education—master’s degree", "Higher education—doctorate", "Frequency of higher education", "12th year of schooling—not completed", "11th year of schooling—not completed", "Other—11th year of schooling",  "10th year of schooling",  "10th year of schooling—not completed",  "Basic education 3rd cycle (9th/10th/11th year) or equivalent",  "Basic education 2nd cycle (6th/7th/8th year) or equivalent",  "Technological specialization course",  "Higher education—degree (1st cycle)",  "Professional higher technical course",  "Higher education—master’s degree (2nd cycle)"],
      nationality: ["Portuguese", "German","Spanish","Italian","Dutch","English","Lithuanian","Angolan","Cape Verdean",
        "Guinean", "Mozambican", "Santomean", "Turkish", "Brazilian", "Romanian", "Moldova (Republic of)", "Mexican",
        "Ukrainian", "Russian", "Cuban", "Colombian"],
      parental_qualification: [ "Unknown", "Basic-level", "Lower-level", "Technical", "Higher-level"],
      parental_occupation: ["Unskilled", "Unknown", "Technical", "Healthcare", "Military", "Administration",
        "Leadership", "Academic"],
      binary: ["Yes", "No"],
      gender: ["Female", "Male"]
    })
    await options.save()
    logger.info("Performance metric options initialised!")
    return true
  } catch (err: any){
    if(err.message && err.message.indexOf('duplicate key error') !== -1){
      logger.error('A set of options already exists with these parameters');
    }
    return false

  }
}