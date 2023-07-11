import {model, Schema} from "mongoose";

export interface IPerformanceMetricOptions {
  name: string;
  marital_status: string[];
  application_mode: string[];
  course: string[];
  attendance_type: string[];
  previous_qualification: string[];
  nationality: string[];
  parental_qualification: string[];
  parental_occupation: string[];
  binary: string[];
  gender: string[];
}

const performanceMetricOptionsSchema = new Schema<IPerformanceMetricOptions>({
  name: {
    type: String,
    required: true,
    unique: true,
    default: 'performanceMetricOptions'
  },
  marital_status: [
    {
      type: String
    }
  ],
  application_mode:  [
    {
      type: String
    }
  ],
  course:  [
    {
      type: String
    }
  ],
  attendance_type:  [
    {
      type: String
    }
  ],
  previous_qualification:  [
    {
      type: String
    }
  ],
  nationality:  [
    {
      type: String
    }
  ],
  parental_qualification:  [
    {
      type: String
    }
  ],
  parental_occupation:  [
    {
      type: String
    }
  ],
  binary: [
    {
      type: String
    }
  ],
  gender: [
    {
      type: String
    }
  ],
}, {
  timestamps: true
})

export const PerformanceMetricOptions = model('PerformanceMetricOptions', performanceMetricOptionsSchema)
