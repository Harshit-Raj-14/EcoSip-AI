/* eslint-disable @next/next/no-img-element */
import * as React from 'react';

import useTrash from '@/store/TrashStore';

import SectionText from '../Text/SectionText';

export default function HistorySection() {
  const store = useTrash();
  const history = store.history;
  console.log(history);
  return (
    <div>
    </div>
  );
}
