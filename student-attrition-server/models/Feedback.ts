import { Schema, model } from "mongoose";

export interface IFeedback {
  _id: Schema.Types.ObjectId
  ipAddress: string;
  content: string;
  consentToDialog: boolean;
  genus: string;
  routeName: string
  status: string;
}

const feedbackSchema = new Schema<IFeedback>({
  ipAddress: {
    type: String,
    required: true
  },
  content: {
    type: String,
    required: true
  },
  consentToDialog: {
    type: Boolean,
    required: true,
    default: false
  },
  genus: {
    type: String,
    required: true,
    default: 'General Feedback'
  },
  routeName: {
    type: String,
    required: true,
  },
  /*
  General Feedback
  Feature Request
  Bug Report
  */
  status: {
    type: String,
    required: true,
    default: 'Active'
  }
  /*
  Active
  Completed
  No Action Required
  */
}, {
  timestamps: true
})

export const Feedback = model<IFeedback>('Feedback', feedbackSchema)